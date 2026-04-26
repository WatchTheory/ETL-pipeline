import os 
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    "source_url" : "API Path here",
    "api_key" : os.getenv("API_KEY"),
    "db_path" : "SQL database path here"
}