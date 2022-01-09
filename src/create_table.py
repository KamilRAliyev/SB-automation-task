import psycopg2
from datetime import datetime
from configurations.db import DATABASE_CONFIGS

current_time = datetime.now()
conn = None

try:
    print(current_time.strftime("%m/%d/%Y, %H:%M:%S"))
    print("-"*10)

    print("1. Connecting to the PostgreSQL database")
    
    # Connection
    conn = psycopg2.connect(**DATABASE_CONFIGS)

    # Creating cursor
    cursor = conn.cursor()    

    # Postgres version
    cursor.execute('SELECT version()')
    db_version = cursor.fetchone()
    print(' +   PostgreSQL database version:',db_version)
    print('\n')

    # Creating table
    name = "stocks"
    print(f"2. Creating table: {name}")
    command = f"""
        CREATE TABLE {name} (
            id SERIAL PRIMARY KEY,
            stock_name VARCHAR(30) NOT NULL, 
            stock_date DATE NOT NULL, 
            _low FLOAT NOT NULL,
            _high FLOAT NOT NULL, 
            _open FLOAT NOT NULL, 
            _close FLOAT NOT NULL, 
            volume FLOAT NOT NULL, 
            insert_date TIMESTAMP NOT NULL
        )
    """
    cursor.execute(command)
    print(' +   Table is created')
    print('\n')

    # close communication with the PostgreSQL database server
    print("3. Closing Database Connection")
    cursor.close()
    # commit the changes
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
        print("Error", error)
finally:
    if conn is not None:
        conn.close()
        print(' +   Database connection closed.')