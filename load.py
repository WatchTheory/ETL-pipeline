from sqlalchemy import create_engine
from config import CONFIG


# Create function to load data into database
def load_data(df):
   # Create databse engine 
    engine = create_engine(f"sqlite:///{CONFIG['db_path']}")
    # Create connection to database
    df.to_sql("resumes", engine, if_exists="append", index=False)

    # print message databse is loaded
    print(f"Loaded {len(df)} rows into database")