import awswrangler as wr
import pandas as pd
import urllib.parse
import os

# Load environment variables
os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name = os.environ['glue_catalog_db_name']
os_input_glue_catalog_table_name = os.environ['glue_catalog_table_name']
os_input_write_data_operation = os.environ['write_data_operation']

def lambda_handler(event, context):
    print("Lambda execution started.")
    
    try:
        # Extract bucket and key from S3 event
        print("Parsing event...")
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        print(f"Bucket: {bucket}")
        print(f"Key: {key}")
        
        # Step 1: Read JSON file from S3
        print("Reading JSON from S3...")
        json_path = f's3://{bucket}/{key}'
        df_raw = wr.s3.read_json(json_path)
        print("Finished reading JSON from S3.")
        print(f"Raw DataFrame shape: {df_raw.shape}")
        
        # Step 2: Normalize nested JSON structure
        print("Normalizing nested JSON using pd.json_normalize...")
        df_step_1 = pd.json_normalize(df_raw['items'])
        print("Finished normalizing JSON.")
        print(f"Normalized DataFrame shape: {df_step_1.shape}")
        
        # Step 3: Write DataFrame to Parquet in S3
        print("Writing DataFrame to S3 as Parquet...")
        wr_response = wr.s3.to_parquet(
            df=df_step_1,
            path=os_input_s3_cleansed_layer,
            dataset=True,
            database=os_input_glue_catalog_db_name,
            table=os_input_glue_catalog_table_name,
            mode=os_input_write_data_operation
        )
        print("Finished writing to S3.")
        print("AWS Wrangler response:", wr_response)

        print("Lambda execution completed successfully.")
        return wr_response

    except Exception as e:
        print("Exception occurred!")
        print(str(e))
        print(f"Error getting object {key} from bucket {bucket}. Make sure it exists and the Lambda has permission.")
        raise e
