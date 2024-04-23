import os
import matplotlib.pyplot as plt 
import streamlit as st
from dotenv import load_dotenv
import pandas as pd
from geopy.geocoders import Nominatim
import folium
import streamlit.components.v1 as components
from utils.b2 import B2
from utils.modeling import *
import networkx as nx  
import seaborn as sns  
import datetime

load_dotenv()

@st.cache_data
def get_data():

    b2 = B2(endpoint=os.environ['B2_ENDPOINT'],
            key_id=os.environ['B2_KEYID'],
            secret_key=os.environ['B2_APPKEY'])
    
    b2.set_bucket(os.environ['B2_BUCKETNAME'])
    df_homicide = b2.get_df(REMOTE_DATA)
    
    agency_data = df_homicide[['Agency Type', 'Crime Solved']]

    agency_counts = agency_data.groupby(['Agency Type', 'Crime Solved']).size().unstack(fill_value=0)
    
    return df_homicide, agency_counts

# Function to geocode the user-entered location
def geocode_location(location):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(location)
    return location.latitude, location.longitude

# Function to search nearby police stations
def search_nearby_police_stations(location):
    # Geocode the user-entered location
    latitude, longitude = geocode_location(location)

    # Create a map centered at the geocoded location
    mymap = folium.Map(location=[latitude, longitude], zoom_start=12)

    # Add a marker for the searched location
    folium.Marker(location=[latitude, longitude], popup=location).add_to(mymap)

    # Placeholder: Fetch nearby police stations based on location (you can replace this with your own logic)
    nearby_stations = fetch_nearby_police_stations(latitude, longitude)

    for station in nearby_stations:
        folium.Marker(location=[station["latitude"], station["longitude"]], popup=station["name"]).add_to(mymap)

    # Get the HTML representation of the map
    map_html = mymap._repr_html_()

    return map_html

# Function to fetch nearby police stations based on coordinates (placeholder)
def fetch_nearby_police_stations(latitude, longitude):
    # Placeholder logic to fetch nearby police stations
    # You can replace this with your own method of fetching nearby police stations
    nearby_stations = [
        {"name": "Police Station 1", "address": "Address 1", "latitude": latitude + 0.01, "longitude": longitude},
        {"name": "Police Station 2", "address": "Address 2", "latitude": latitude - 0.01, "longitude": longitude},
        {"name": "Police Station 3", "address": "Address 3", "latitude": latitude, "longitude": longitude + 0.01}
    ]
    return nearby_stations

# Network Building Function
def build_network(data):
    # Create an empty graph
    G = nx.Graph()
    
    # Add nodes for individuals (victims, perpetrators) and relationships
    for index, row in data.iterrows():
        # Add victim node
        victim = row['Victim Race']
        G.add_node(victim)
        
        # Add perpetrator node
        perpetrator = row['Perpetrator Race']
        G.add_node(perpetrator)
        
        # Add relationship as edge
        relationship = row['Relationship']
        G.add_edge(victim, perpetrator, relationship=relationship)
    
    return G

# Visualization Function for Network
def visualize_network(G):
    # Plot the network
    fig, ax = plt.subplots(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', linewidths=1, font_size=10, ax=ax)
    ax.set_title("Homicide Case Network")
    st.pyplot(fig)

REMOTE_DATA = 'homicide2.csv'
df_homicide, agency_counts = get_data()

#for sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Statistical Reports", "Nearby Police Departments", "Crime Victim Support Organizations", "Emergency Contacts", "Network Analysis"))

st.title("TonksGuard Web App")

# Initialize session state
if "report_index" not in st.session_state:
    st.session_state.report_index = 0

if page == "Statistical Reports":
    st.header("Statistical Reports")

    # Define a list of statistical reports
    reports = [
        {"title": "Yearly Crime Trends", "data": df_homicide.groupby('Year').size()},
        {"title": "Crime Types Distribution", "data": df_homicide['Crime Type'].value_counts()},
        {"title": "Relationship Analysis", "data": df_homicide['Relationship'].value_counts()},
        {"title": "Weapon Usage Patterns", "data": df_homicide['Weapon'].value_counts()}
    ]

    # Display the current report
    st.subheader(reports[st.session_state.report_index]["title"])
    st.bar_chart(reports[st.session_state.report_index]["data"])

    # Add navigation buttons
    col1, col2, col3 = st.columns([1, 8, 1])
    with col1:
        if st.session_state.report_index > 0:
            if st.button("< Previous"):
                st.session_state.report_index -= 1
    with col2:
        st.write("")  # Add empty space for layout
    with col3:
        if st.session_state.report_index < len(reports) - 1:
            if st.button("Next >"):
                st.session_state.report_index += 1

elif page == "Nearby Police Departments":
    st.header("Nearby Police Departments")
    # Placeholder for mapping feature
    search_location = st.text_input("Enter your location or incident location:")
    if st.button("Search"):
        map_html = search_nearby_police_stations(search_location)
        components.html(map_html, height=600)

elif page == "Network Analysis":
    st.header("Network Analysis")
    
    # Build the network
    network = build_network(df_homicide)
    
    # Visualize the network
    visualize_network(network)

elif page == "Crime Victim Support Organizations":
    st.header("Crime Victim Support Organizations")
    st.markdown("- [Victim Support](https://www.victimsupport.org.uk/)")
    st.markdown("- [National Center for Victims of Crime](https://victimsofcrime.org/)")
    st.markdown("- [RAINN (Rape, Abuse & Incest National Network)](https://www.rainn.org/)")
    st.markdown("- [NOVA (National Organization for Victim Assistance)](https://www.trynova.org/)")

elif page == "Emergency Contacts":
    st.header("Emergency Contacts")
    st.markdown("- [Emergency Helpline](tel:911)")
    st.markdown("- [National Suicide Prevention Lifeline](tel:1-800-273-TALK)")
    st.markdown("- [Emergency Medical Services](tel:911)")
    st.markdown("- [Domestic Violence Hotline](tel:1-800-799-SAFE)")

st.sidebar.text("TonksGuard Web App")

