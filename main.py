from google.cloud import bigquery
from google.oauth2 import service_account

key_path  = r'gdelt-420506-810460212886.json'

# Create credentials using the key file
credentials = service_account.Credentials.from_service_account_file(key_path)

# Create a client
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

dataset_ref = client.dataset("gdeltv2", project="gdelt-bq")
dataset = client.get_dataset(dataset_ref)
tables = list(client.list_tables(dataset))
for table in tables:  
    print(table.table_id)