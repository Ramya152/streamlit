<h1>TonksGuard Web App</h1>

TonksGuard Web App is a Streamlit application that provides various functionalities related to homicide data analysis, crime victim support organizations, emergency contacts, and network analysis of individuals involved in the homicide cases.

The data used in the TonksGuard Web App is extracted from a dataset in Kaggle which contains information about homicide incidents.<br />
Link for dataset: https://www.kaggle.com/datasets/murderaccountability/homicide-reports/data<br />
The dataset includes attributes such as agency type, location, crime type, victim and perpetrator demographics, relationship between victim and perpetrator, and weapon used. Before analysis, the data is cleaned to remove missing values and ensure consistency.

Link for my streamlit app : https://app-xappg7tbf7wxzbb5e6hjv97.streamlit.app/

<h3>Tools Used</h3>
The TonksGuard Web App is built using the following tools:

<b>Python</b>: Used pythoin to develop the web application and implement data analysis algorithms. <br />
<b>Streamlit</b>: It is a python library used for creating interactive web applications with simple python scripts.<br />
<b>Pandas</b>: Python library for data manipulation and analysis.<br />
<b>Matplotlib</b>: Python plotting library for creating static, interactive, and animated visualizations.<br />
<b>Folium</b>: Python library for creating interactive maps.<br />
<b>Geopy</b>: Python library for geocoding and working with geographical data.

<h3>Algorithm Description</h3>
The main algorithms in TonksGuard Web App are:

<b>Network Building Algorithm:</b> This algorithm builds networks of individuals involved in homicide cases based on victim-perpetrator relationships.<br />
<b>Police Station Search Algorithm:</b> Utilizes Geopy to search for nearby police stations based on user-entered location.

<h2>Features</h2>

<h3>Statistical Reports</h3>

<b>Yearly Crime Trends:</b> Visualizes the yearly trends of homicide incidents.<br />
<b>Crime Types Distribution:</b> Shows the distribution of different crime types.<br />
<b>Relationship Analysis:</b> Analyzes the relationships between victims and perpetrators.<br />
<b>Weapon Usage Patterns:</b> Presents the distribution of weapons used in homicide cases.

<h3>Nearby Police Departments</h3>
Enables users to search for nearby police departments based on location or incident location.

<h3>Network Analysis</h3>
Builds networks of individuals involved in homicide cases (victims, suspects) and analyzes their connections.

<h3>Crime Victim Support Organizations</h3>
Provides links to various crime victim support organizations for assistance and resources.

<h3>Emergency Contacts</h3>
Lists emergency contact numbers for immediate help in critical situations.

<h2>Usage Example</h2>
Imagine you're a new resident in a city and want to explore the safety and crime statistics of different neighborhoods. You can use TonksGuard Web App to analyze crime trends, find nearby police departments for each neighborhood, and access emergency contacts in case of any safety concerns. Additionally, if you need support or assistance related to crime victimization, you can easily find information about relevant support organizations through the application.

<h2>How to Run</h2>
To run the TonksGuard Web App locally, follow these steps:
1. Clone the repository to your local machine.
2. Install the required dependencies using pip install -r requirements.txt.
3. Set up environment variables for accessing crime datasets and geolocation services.
4. Run the application using streamlit run app.py.

<h3>Contributing</h3>
Contributions to TonksGuard Web App are welcome! If you have suggestions for new features, bug fixes, or improvements, please submit a pull request or open an issue on GitHub.

<h3>Ethical Concerns</h3>
1. The homicide dataset used may contain sensitive information about victims and perpetrators. To mitigate privacy risks, personal identifiers such as names and addresses are not displayed, and only aggregate information is presented.<br />
2. There also may be biases in the data collection process in the criminal justice system reflected in the dataset. To address this, stakeholders should interpret the results with caution and consider potential biases when making decisions based on the analysis.


