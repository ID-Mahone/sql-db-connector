import pyodbc
import pandas as pd

class SQLDB:
    def __init__(self,
                 server="local",
                 integrated_security=True,
                 driver="{ODBC Driver 13 for SQL Server}",
                 dbname="",
                 username="",
                 password=""):
        self.server = server
        self.integrated_security = integrated_security
        self.driver = driver
        self.dbname = dbname
        self.username = username
        self.password = password

        # Initializing connection string
        self.connstring = f"Driver={self.driver};Server={self.server};Database={self.dbname};Trusted_Connection=yes"

        # If not using integrated security, include UID and PWD
        if not integrated_security:
            self.connstring += f";UID={self.username};PWD={self.password}"

    def get_db_data(self, sqlstatement):
        """Run the query and return results as a DataFrame."""
        try:
            # Establishing connection
            conn = pyodbc.connect(self.connstring)
            result = pd.read_sql(sqlstatement, conn)
            conn.close()
            return result
        except Exception as e:
            print(f"Error: {e}")
            return None
