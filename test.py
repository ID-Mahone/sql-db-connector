import unittest
from SQLDB import SQLDB
import pandas as pd
from unittest.mock import patch, MagicMock

class TestSQLDB(unittest.TestCase):

    @patch("pyodbc.connect")
    def test_get_db_data_success(self, mock_connect):
        # Mock a successful database connection
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.execute.return_value = None
        mock_cursor.fetchall.return_value = [(1, 'John'), (2, 'Jane')]

        # Instantiate the SQLDB class
        db = SQLDB(server="localhost", dbname="YourDatabase", integrated_security=True)

        # Define a mock SQL query
        sql_query = "SELECT id, name FROM users"

        # Call the method under test
        result = db.get_db_data(sql_query)

        # Assert that the result is a Pandas DataFrame
        self.assertIsInstance(result, pd.DataFrame)

        # Assert that the DataFrame has the expected values
        self.assertEqual(result.shape, (2, 2))  # 2 rows, 2 columns
        self.assertEqual(result.iloc[0, 1], "John")
        self.assertEqual(result.iloc[1, 1], "Jane")

        # Check that the database connection was properly closed
        mock_conn.close.assert_called_once()

    @patch("pyodbc.connect")
    def test_get_db_data_failure(self, mock_connect):
        # Simulate a connection failure
        mock_connect.side_effect = Exception("Connection failed")

        db = SQLDB(server="localhost", dbname="YourDatabase", integrated_security=True)

        sql_query = "SELECT id, name FROM users"
        result = db.get_db_data(sql_query)

        # Assert that the result is None due to the error
        self.assertIsNone(result)

    @patch("pyodbc.connect")
    def test_invalid_sql_query(self, mock_connect):
        # Mock a successful connection
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.execute.return_value = None
        mock_cursor.fetchall.side_effect = Exception("SQL query failed")

        db = SQLDB(server="localhost", dbname="YourDatabase", integrated_security=True)
        sql_query = "INVALID SQL"
        result = db.get_db_data(sql_query)

        # Assert that the result is None due to the invalid SQL query
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
