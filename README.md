<h1>TonksGuard Web App</h1>

TonksGuard Web App is a Streamlit application designed to provide various functionalities related to homicide data analysis, crime victim support organizations, emergency contacts, and network analysis of individuals involved in the homicide cases.

The data used in the TonksGuard Web App is extracted from a dataset containing information about homicide incidents. The dataset includes attributes such as agency type, location, crime type, victim and perpetrator demographics, relationship between victim and perpetrator, and weapon used. Before analysis, the data is cleaned to remove missing values and ensure consistency.

<h3>Tools Used</h3>
The TonksGuard Web App is built using the following tools:

Python: The primary programming language for developing the web application and implementing data analysis algorithms.
Streamlit: A Python library used for creating interactive web applications with simple Python scripts.
Pandas: A Python library for data manipulation and analysis.
Matplotlib: A Python plotting library for creating static, interactive, and animated visualizations.
Folium: A Python library for creating interactive maps.
Geopy: A Python library for geocoding and working with geographical data.

<h3>Algorithm Description</h3>
The main algorithms driving the TonksGuard Web App are:

Network Building Algorithm: This algorithm builds networks of individuals involved in homicide cases based on victim-perpetrator relationships.
Time Series Analysis Algorithm: This algorithm performs time series analysis to explore patterns and trends in homicide incidents over time.
Police Station Search Algorithm: Utilizes Geopy, a Python library for geocoding, to search for nearby police stations based on user-entered location or incident location.

<h2>Features</h2>

<h3>Statistical Reports</h3>

<b>Yearly Crime Trends:</b> Visualizes the yearly trends of homicide incidents.
<b>Crime Types Distribution:</b> Shows the distribution of different crime types.
<b>Relationship Analysis:</b> Analyzes the relationships between victims and perpetrators.
<b>Weapon Usage Patterns:</b> Presents the distribution of weapons used in homicide cases.

<h3>Nearby Police Departments</h3>
Enables users to search for nearby police departments based on location or incident location.

<h3>Network Analysis</h3>
Builds networks of individuals involved in homicide cases (e.g., victims, suspects, witnesses) and analyzes their connections.

<h3>Crime Victim Support Organizations</h3>
Provides links to various crime victim support organizations for assistance and resources.

<h3>Emergency Contacts</h3>
Lists emergency contact numbers for immediate help in critical situations.

<h3>Ethical Concerns</h3>
Data Privacy: The homicide dataset used in the TonksGuard Web App may contain sensitive information about victims and perpetrators. To mitigate privacy risks, personal identifiers such as names and addresses are not displayed, and only aggregate information is presented.
Bias and Fairness: There may be biases in the data collection process or inherent biases in the criminal justice system reflected in the dataset. To address this, stakeholders should interpret the results with caution and consider potential biases when making decisions based on the analysis.
User Interface Accessibility: The web application should be designed to be accessible to all users, including those with disabilities. Providing alternative text for images, ensuring keyboard navigation, and using color schemes that are accessible to individuals with color vision deficiencies are essential considerations.


