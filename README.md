<h1>TonksGuard Web App</h1>

TonksGuard Web App is a Streamlit application that provides various functionalities related to homicide data analysis, crime victim support organizations, emergency contacts, and network analysis of individuals involved in the homicide cases.

The data used in the TonksGuard Web App is extracted from a dataset in Kaggle which contains information about homicide incidents.
Link for dataset: https://www.kaggle.com/datasets/murderaccountability/homicide-reports/data
The dataset includes attributes such as agency type, location, crime type, victim and perpetrator demographics, relationship between victim and perpetrator, and weapon used. Before analysis, the data is cleaned to remove missing values and ensure consistency.

<h3>Tools Used</h3>
The TonksGuard Web App is built using the following tools:

<b>Python</b>: Used pythoin to develop the web application and implement data analysis algorithms.
<b>Streamlit</b>: It is a python library used for creating interactive web applications with simple python scripts.
<b>Pandas</b>: Python library for data manipulation and analysis.
<b>Matplotlib</b>: Python plotting library for creating static, interactive, and animated visualizations.
<b>Folium</b>: Python library for creating interactive maps.
<b>Geopy</b>: Python library for geocoding and working with geographical data.

<h3>Algorithm Description</h3>
The main algorithms in TonksGuard Web App are:

<b>Network Building Algorithm:</b> This algorithm builds networks of individuals involved in homicide cases based on victim-perpetrator relationships.
<b>Police Station Search Algorithm:</b> Utilizes Geopy to search for nearby police stations based on user-entered location.

<h2>Features</h2>

<h3>Statistical Reports</h3>

<b>Yearly Crime Trends:</b> Visualizes the yearly trends of homicide incidents.
<b>Crime Types Distribution:</b> Shows the distribution of different crime types.
<b>Relationship Analysis:</b> Analyzes the relationships between victims and perpetrators.
<b>Weapon Usage Patterns:</b> Presents the distribution of weapons used in homicide cases.

<h3>Nearby Police Departments</h3>
Enables users to search for nearby police departments based on location or incident location.

<h3>Network Analysis</h3>
Builds networks of individuals involved in homicide cases (victims, suspects) and analyzes their connections.

<h3>Crime Victim Support Organizations</h3>
Provides links to various crime victim support organizations for assistance and resources.

<h3>Emergency Contacts</h3>
Lists emergency contact numbers for immediate help in critical situations.

<h3>Ethical Concerns</h3>
1. The homicide dataset used may contain sensitive information about victims and perpetrators. To mitigate privacy risks, personal identifiers such as names and addresses are not displayed, and only aggregate information is presented.
2. There also may be biases in the data collection process in the criminal justice system reflected in the dataset. To address this, stakeholders should interpret the results with caution and consider potential biases when making decisions based on the analysis.


