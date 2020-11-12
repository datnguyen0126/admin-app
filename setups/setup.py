import sqlite3
from pathlib import Path
import sys
# Set up Database Tables
PARENT_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(PARENT_PATH))
from models.config import Configurations


def Setup_database_tables(path):
    "Creates tables for the Database"
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS LoginInfo
                 (Username TEXT, Password TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS Instruments
                 (name TEXT, displayName TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS All_Transactions
                 (id TEXT, name TEXT, quantity REAL, price REAL, pnl REAL,
                  cancelled INTEGER)""")
    conn.commit()
    c.close()
    conn.close()
    print(f"A new database has been created in {path}")


def check_configurations():
    "Checks if the APIs have been set up."
    c = Configurations()
    config_database = c.DATABASE_NAME
    if config_database == "":
        raise ValueError("The application is not connected to a database. "
                         "Please set a database name to the config file.")
    print(f"Connected to {config_database}")
