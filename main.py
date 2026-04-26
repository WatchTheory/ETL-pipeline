from extract import extract_data
from transform import transform_data
from load import load_data
import logging

logging.basicConfig(level=logging.INFO)


# Main function to run the pipeline
def run_pipeline():

    # Step 0: starting the pipeline
    print("Starting Pipeline...")

    # Step 1: Extract data
    raw_df = extract_data()
    if raw_df is None:
        logging.error("Data extraction failed.")
        return False
    
    # Step 2: Transform data
    cleaned_df = transform_data(raw_df)

    # Step 3: Load data 
    load_data = load_data(cleaned_df)
    # Step 4: Finished the Pipeline
    print("Pipeline finished successfully!")

    # if pipeline is successful, return True else return False

    # if step 1 fails, return False 

    # if step 2 fails, return False 

    # if step 3 fails, return False 

    # if steps 4 fails, return False



# def main():
#     print("Hello from pipeline!")


if __name__ == "__main__":
    run_pipeline()
