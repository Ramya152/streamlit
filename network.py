import networkx as nx
import matplotlib.pyplot as plt 
import streamlit as st
def build_network(data):
    G = nx.Graph()
    

    for index, row in data.iterrows():
       
        victim = row['Victim Race']
        G.add_node(victim)
        
       
        perpetrator = row['Perpetrator Race']
        G.add_node(perpetrator)
        
       
        relationship = row['Relationship']
        G.add_edge(victim, perpetrator, relationship=relationship)
    
    return G


def visualize_network(G):
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 8))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', linewidths=1, font_size=10, ax=ax)
    ax.set_title("Homicide Case Network")
    st.pyplot(fig)