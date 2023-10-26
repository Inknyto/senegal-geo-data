import wbdata
import matplotlib.pyplot as plt
 
#set up the countries I want
countries = ["CAN","FRA","NIC", "SEN"]
 
#set up the indicator I want (just build up the dict if you want more than one)
indicators = {'NY.GNP.PCAP.CD':'GNI per Capita'}
 
#grab indicators above for countires above and load into data frame
df = wbdata.get_dataframe(indicators, country=countries, convert_date=False)

#df is "pivoted", pandas' unstack fucntion helps reshape it into something plottable
dfu = df.unstack(level=0)

# a simple matplotlib plot with legend, labels and a title
dfu.plot(); 
plt.legend(loc='best'); 
plt.title("GNI Per Capita ($USD, Atlas Method)"); 
plt.xlabel('Date'); plt.ylabel('GNI Per Capita ($USD, Atlas Method');
import requests
import pandas as pd

# Step 2: Send an HTTP GET request to the web page
url = 'https://unstats.un.org/unsd/methodology/m49/'  # Replace with the URL of the web page containing the table
response = requests.get(url)

# Step 3: Check if the request was successful and retrieve the page content
if response.status_code == 200:
    page_content = response.content
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
    exit()  # You can handle the error as needed

# Step 4: Parse the HTML content to extract the table
tables = pd.read_html(page_content)
# You may need to inspect the list of tables to identify the one you want to use
table_df = tables[0]  # Assuming the first table on the page is the one you want

# Now you can work with the table_df DataFrame as needed.
