import requests
import pandas as pd
from config import CONFIG


# Function to extract data from the API
def extract_data():
# The client sends a GET request to the API endpoint 
     requests = requests.get(
        CONFIG['source_url'],
         # the header contains the API key for authentication; to make sure you are who you say you are.
        headers={"Authorization": f"Bearer {CONFIG['api_key']}"},
        # the process is timeout at 30 seconds.
        timeout=30
     )
     requests.raise_for_status()  # Check if the request was successful
  
# Convert the Dataframe immediately to pandas DataFrame
df = pd.DataFrame(requests.json()["data"])
df.to_parquet("data/raw/latest_extract.parquest")   # save the data in Parquest format(columnar storage) 