import os
import matplotlib.pyplot as plt 
import streamlit as st
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
import folium
import streamlit.components.v1 as components
from utils.b2 import B2

from ps import search_nearby_police_stations
from network import build_network, visualize_network
import seaborn as sns  
import datetime

load_dotenv()

class TonksGuardApp:
    REMOTE_DATA = 'Homicide Report.csv'

    def __init__(self):
        self.df_homicide, self.agency_counts = self.get_data()
        if "report_index" not in st.session_state:
            st.session_state.report_index = 0

    @staticmethod
    @st.cache
    def get_data():
        b2 = B2(endpoint=os.environ['B2_ENDPOINT'],
                key_id=os.environ['B2_KEYID'],
                secret_key=os.environ['B2_APPKEY'])
        
        b2.set_bucket(os.environ['B2_BUCKETNAME'])
        df_homicide = b2.get_df(TonksGuardApp.REMOTE_DATA)
        
        agency_data = df_homicide[['Agency Type', 'Crime Solved']]
        agency_counts = agency_data.groupby(['Agency Type', 'Crime Solved']).size().unstack(fill_value=0)
        
        return df_homicide, agency_counts

    def handle_error(self, error_message):
        st.error(f"An error occurred: {error_message}")

    def run(self):
        # Sidebar navigation
        st.sidebar.title("Navigation")
        page = st.sidebar.radio("Go to", ("Statistical Reports", "Nearby Police Departments", "Crime Victim Support Organizations", "Emergency Contacts", "Network Analysis"))

        st.title("TonksGuard Web App")

        # Page routing
        if page == "Statistical Reports":
            self.statistical_reports_page()
        elif page == "Nearby Police Departments":
            self.nearby_police_departments_page()
        elif page == "Network Analysis":
            self.network_analysis_page()
        elif page == "Crime Victim Support Organizations":
            self.crime_victim_support_orgs_page()
        elif page == "Emergency Contacts":
            self.emergency_contacts_page()

        st.sidebar.text("TonksGuard Web App")

    def statistical_reports_page(self):
        """
        Displays various statistical reports related to homicide data.
        Users can navigate through different reports using navigation buttons.
        """
        st.header("Statistical Reports")
        st.write("Explore different statistical reports based on homicide data.")
        try:
            # list of statistical reports
            reports = [
                {"title": "Yearly Crime Trends", "data": self.df_homicide.groupby('Year').size()},
                {"title": "Crime Types Distribution", "data": self.df_homicide['Crime Type'].value_counts()},
                {"title": "Relationship Analysis", "data": self.df_homicide['Relationship'].value_counts()},
                {"title": "Weapon Usage Patterns", "data": self.df_homicide['Weapon'].value_counts()}
            ]

            # current report
            st.subheader(reports[st.session_state.report_index]["title"])
            st.bar_chart(reports[st.session_state.report_index]["data"])

            # navigation buttons
            col1, col2, col3 = st.columns([1, 8, 1])
            with col1:
                if st.session_state.report_index > 0:
                    if st.button("< Previous"):
                        st.session_state.report_index -= 1
            with col2:
                st.write("") 
            with col3:
                if st.session_state.report_index < len(reports) - 1:
                    if st.button("Next >") or  st.session_state.report_index==0:
                        st.session_state.report_index += 1
        except Exception as e:
            self.handle_error(str(e))

    def nearby_police_departments_page(self):
        """
        Displays a map with nearby police stations based on user input location.
        """
        st.header("Nearby Police Departments")
        st.write("Find nearby police departments based on your location.")
        # placeholder for mapping feature
        search_location = st.text_input("Enter your location or incident location:")
        if st.button("Search"):
            map_html = search_nearby_police_stations(search_location)
            components.html(map_html, height=600)

    def network_analysis_page(self):
        """
        Performs network analysis on homicide data and visualizes the network.
        """
        st.header("Network Analysis")
        st.write("Analyze networks of individuals involved in homicide cases.")
        network = build_network(self.df_homicide)
        visualize_network(network)

    def crime_victim_support_orgs_page(self):
        """
        Displays information about crime victim support organizations.
        """
        st.header("Crime Victim Support Organizations")
        st.write("Access information about organizations providing support to crime victims.")
        st.markdown("- [Victim Support](https://www.victimsupport.org.uk/)")
        st.markdown("- [National Center for Victims of Crime](https://victimsofcrime.org/)")
        st.markdown("- [RAINN (Rape, Abuse & Incest National Network)](https://www.rainn.org/)")
        st.markdown("- [NOVA (National Organization for Victim Assistance)](https://www.trynova.org/)")

    def emergency_contacts_page(self):
        """
        Displays emergency contact information.
        """
        st.header("Emergency Contacts")
        st.write("Access emergency contact information for immediate assistance.")
        st.markdown("- [Emergency Helpline](tel:911)")
        st.markdown("- [National Suicide Prevention Lifeline](tel:1-800-273-TALK)")
        st.markdown("- [Emergency Medical Services](tel:911)")
        st.markdown("- [Domestic Violence Hotline](tel:1-800-799-SAFE)")

if __name__ == "__main__":
    app = TonksGuardApp()
    app.run()
