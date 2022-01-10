from configurations.db import DATABASE_CONFIGS
from configurations.api import API_KEY

import os
import psycopg2
import csv

if __name__ == "__main__":

    conn = None

    try:
        conn = psycopg2.connect(**DATABASE_CONFIGS)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM stocks FETCH FIRST 100 ROW ONLY')

        result = cursor.fetchall()
        print(result[1])

        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(" Error:", error)
    finally:
        if conn is not None:
            conn.close()

    file_path = os.path.dirname(os.path.realpath(__file__))
    path = file_path + "/outputs/"

    with open(f'{path}gathered_data.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(['stock name', 'date', 'low', 'high', 'open', 'close', 'volume'])
        for record in result:            
            data = record[1:8]
            writer.writerow(data)

        f.close()