import pandas as pd
from sqlalchemy import create_engine

# Read CSV file into Pandas DataFrame
csv_file_path = r'C:\Users\Patrick\Desktop\DEV\datasets\WWI\raw_application_delivery_method.csv'
df = pd.read_csv(csv_file_path)

# Connect to PostgreSQL database
db_user = 'etl_user'
db_password = 'password123'
db_host = 'localhost'
db_name = 'WideWorldImporters'

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}', echo=True)

# Define table name and schema
table_name = 'delivery_method'  # Replace with your desired table name
schema_name = 'raw'

# Load data into PostgreSQL
df.to_sql(table_name, engine, schema=schema_name, if_exists='replace', index=False)

print("Data loaded successfully into PostgreSQL!")
