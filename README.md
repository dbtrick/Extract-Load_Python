### Project Overview:

For this project, I worked with a sample client, WideWorldImporters, to manage their business data. Using various tools and technologies, I created a streamlined workflow for data extraction and loading. The dataset provided by WideWorldImporters includes comprehensive information about their business operations, available at the following link: [WideWorldImporters Sample Datasets.](https://github.com/Microsoft/sql-server-samples/releases/tag/wide-world-importers-v1.0)

![modern-data-stack (6)](https://github.com/dbtrick/Extract-Load_Python/assets/172040645/fdfe9ef8-4a72-418d-9889-8ce82a5100be)
## Key Components and Workflow:
### Data Extraction from SQL Server (WideWorldImporters dataset):
- Utilizes Python libraries like pyodbc to connect to SQL Server.
- Executes SQL queries to extract data based on defined criteria or tables.
- Extracts data from WideWorldImporters dataset to provide insights into various business operations.

### Data Extraction from Different File Formats (CSV and Excel):
- Uses Python pandas to read various file formats such as CSV and Excel.
- Integrates data from different file formats to ensure comprehensive data extraction.

### Data Loading into PostgreSQL:
- Uses Python psycopg2 to establish connection with PostgreSQL.
- Inserts or updates data into PostgreSQL tables based on predefined mappings or business logic.
- Stores the extracted data in PostgreSQL for further use.
