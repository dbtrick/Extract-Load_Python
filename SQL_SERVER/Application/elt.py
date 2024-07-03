from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import pandas as pd
import os

uid = 'etl_user'
pwd = 'password123'
# uid = os.environ['PG_USER']
# pwd = os.environ['PG_PASSWORD']

driver = 'SQL Server'
server = 'localhost'
database = 'WideWorldImporters'

# Extract data from SQL Server
def extract():
    try:
        connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={uid};PWD={pwd}'
        connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
        src_engine = create_engine(connection_url)
        src_conn = src_engine.connect()
        # Execute query
        query = """
        SELECT t.name AS table_name
        FROM sys.tables t
        WHERE t.name IN ('TransactionTypes')
        """
        src_tables = pd.read_sql_query(query, src_conn).to_dict()['table_name']

        for id in src_tables:
            table_name = src_tables[id]
            schema_name = 'Application'
            df = pd.read_sql_query(f'SELECT * FROM {schema_name}.{table_name}', src_conn)
            load(df, table_name)

    except Exception as e:
        print("Data extract error: " + str(e))

# Load data to PostgreSQL
def load(df, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:5432/WideWorldImporters')
        print(f'Importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
        # Save df to PostgreSQL
        df.to_sql(f'raw_{tbl}', engine, schema='raw', if_exists='replace', index=False, chunksize=100000)
        rows_imported += len(df)
        # Add elapsed time to final print out
        print("Data imported successfully")
    except Exception as e:
        print("Data load error: " + str(e))

try:
    # Call extract function
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))

