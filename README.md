# sql-db-connector
 class for connecting to and interacting with a SQL Server database

## Overview

The `SQLDB` Python class provides a simple and reusable interface for interacting with SQL Server databases. This class is designed to abstract the complexity of database connection management and data retrieval. It allows you to connect to a SQL Server, execute queries, and return results as a Pandas DataFrame for further analysis or processing.

## Purpose

As part of my data engineering tools, this class enables efficient interaction with SQL Server databases in Python. It encapsulates the logic for database connections, query execution, and error handling, which reduces the boilerplate code needed when working with SQL Server databases.

## Features

- **Flexible Authentication**: Supports both Windows Authentication and SQL Server Authentication.
- **SQL Query Execution**: Allows for seamless execution of SQL queries directly from Python and returns the result as a Pandas DataFrame.
- **Error Handling**: Robust error handling during connection and query execution.
- **Reusable**: Designed to be used as a utility class in any data processing pipeline or report generation task.

## Prerequisites

- Python 3.x
- Required Libraries:
  - `pyodbc`: For SQL Server database connectivity via ODBC.
  - `pandas`: For handling query results as DataFrames.

To install these dependencies, use the following command:

```bash
pip install pyodbc pandas
```

## Installation

To integrate the `SQLDB` class into your project:

1. Clone or download the `SQLDB.py` file to your project directory.
2. Import the class into your script:
   ```python
   from SQLDB import SQLDB
   ```

## Usage

### Step 1: Create the SQLDB Class

Create an instance of the `SQLDB` class by providing the required connection parameters:

```python
db = SQLDB(
    server="localhost",               # SQL Server hostname or IP
    dbname="YourDatabaseName",         # Database name
    integrated_security=True,          # Set to False for SQL Server authentication
    username="your_username",          # Only required if integrated_security=False
    password="your_password"           # Only required if integrated_security=False
)
```

### Step 2: Execute a Query

Use the `get_db_data` method to execute a SQL query and retrieve the results as a Pandas DataFrame:

```python
sql_query = "SELECT * FROM your_table"
data = db.get_db_data(sql_query)

if data is not None:
    print(data)
else:
    print("Failed to retrieve data.")
```

### Step 3: Handling Query Results

The query results will be returned as a Pandas DataFrame, which you can manipulate, visualize, or export as needed:

```python
# Example: Save the query results to a CSV file
data.to_csv("output.csv", index=False)
```

## Example Script

```python
from SQLDB import SQLDB

if __name__ == "__main__":
    # Connect to the database
    db = SQLDB(server="localhost", dbname="YourDBName", integrated_security=True)

    # Define the SQL query
    sql_query = "SELECT * FROM your_table_name"

    # Execute the query and retrieve data
    data = db.get_db_data(sql_query)

    # Print the results
    if data is not None:
        print(data)
    else:
        print("Query failed.")
```

## Error Handling

The `get_db_data` method contains built-in error handling. If the connection fails or the SQL query encounters an error, the method will output the error message and return `None`. Be sure to check the return value and handle errors as appropriate in your code.

## Contributing

Contributions to the `SQLDB` class are welcome. Please ensure any contributions adhere to the following guidelines:

- Fork the repository and create a feature branch.
- Ensure the code passes all relevant tests.
- Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

David Manning
