import pytest
from lib.database_connection import DatabaseConnection

# This is a Pytest fixture.
# It creates an object that we can use in our tests.
# We will use it to create a database connection.
@pytest.fixture
def db_connection():
    conn = DatabaseConnection()
    conn.connect()
    return conn