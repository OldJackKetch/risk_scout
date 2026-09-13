import sqlite3
import os

## Define the local database
DB_FILE = 'local_database.db'

def initialize_database():
    print(f"[temuSkyNet] Initializing local database framework...")
    
    ## Connect to SQLite. If the fiule doesn't exist, SQLite will automatically create it
    connection = sqlite3.connect(DB_FILE)

    ## The cursor allows us to execute raw SQL commands withinn the Python script
    cursor = connection.cursor()

    print("[temuSkyNet] Creating database schema tables... ")

    ## Write the SQL query to build the structural risk table
    ## This matches the schemapreviously mapped

    create_table_query = """
    CREATE TABLE IF NOT EXISTS applicant_risk_profiles (
        applicant_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        age INTEGER NOT NULL,
        annual_income REAL NOT NULL,
        total_debt REAL NOT NULL,
        debt_to_income_ratio REAL NOT NULL,
        underwriting_flag TEXT NOT NULL
    );
    """

    try:
        ## Exceute the table creation SQL command
        cursor.execute(create_table_query)

        ## Save (commit) the structural changes to the database file
        connection.commit()
        print(f"[success] Database '{DB_FILE}' generated smoothly with applicant_risk_profiles' table.")

    except sqlite3.Error as error:
        print(f"[Failure] An error occured while creating the table: {error}")

    finally:
        ## Close the database when finished to prevent file locks
        connection.close()
        print("[System] Database connection closed successfully.")

if __name__ == "__main__":
    initialize_database()



