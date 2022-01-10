import requests
import psycopg2
import os
import json
from datetime import datetime

ELEMENT_STRUCTURE = {
            "open": "1. open",
            "high": "2. high",
            "low": "3. low",
            "close": "4. close",
            "volume": "5. volume"
        }

class ApiSeeder:
    api_url = "https://www.alphavantage.co/query?"

    def __init__ (self, api_key, database_configs, stock_name, data_type):
        # Basic Configurations
        self.api_key = api_key
        self.database_configs = database_configs
        
        # Data Information
        self.stock_name = stock_name
        self.data_type = data_type

    def fetch_data(self, function):
        # generate url query
        self.query = f"{self.api_url}function={function}&symbol={self.stock_name}&apikey={self.api_key}&datatype={self.data_type}"
        
        # request
        req = requests.get(self.query)
        self.insert_date =  datetime.now()
        self.data = req.json()
    
    def _output_json(self):
        filename_format = f"result_{self.stock_name}_%d-%B-%Y_%H-%M.json"
        file_path = os.path.dirname(os.path.realpath(__file__))
        parent_path = os.path.abspath(os.path.join(file_path, os.pardir))
        path = parent_path + "/outputs/results/"+self.insert_date.strftime(filename_format)
        with open(path, "w") as result_file:
            json.dump(self.data, result_file)
        result_file.close()

    def _generate_values(self):
        time_series = self.data["Monthly Time Series"]
        insert_date = self.insert_date.strftime("%Y-%m-%d %H:%M:%S")
        
        lst = []

        for count, value in enumerate(time_series):
            element = time_series[value]

            e_high = element[ELEMENT_STRUCTURE["high"]]
            e_open = element[ELEMENT_STRUCTURE["open"]]
            e_low = element[ELEMENT_STRUCTURE["low"]]
            e_close = element[ELEMENT_STRUCTURE["close"]]
            e_volume = element[ELEMENT_STRUCTURE["volume"]]

            lst.append((self.stock_name, value, e_low, e_high, e_open, e_close, e_volume, insert_date))
        
        self.values = lst
    
    
    def push_to_database(self):
        print(f"Push to database: {self.insert_date}")
        
        values = self.values
        
        #command = "INSERT INTO stocks VALUES"
        conn = None

        try:
            print("1. Connecting to PostgreSQL")
            # Connection
            conn = psycopg2.connect(**self.database_configs)
            # Creation cursor
            cursor = conn.cursor()

            args = ",".join(cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s)", i).decode('utf-8') for i in values)

            cursor.execute("INSERT INTO stocks(stock_name, stock_date, _low, _high, _open, _close, volume, insert_date) VALUES" + (args))
            
            # Commit the changes
            conn.commit()

            # Close communications
            conn.close()
            print(f" +   Inserted {len(values)} row(s).")
        except (Exception, psycopg2.DatabaseError) as error:
            print(" Error:", error)
        finally:
            if conn is not None:
                conn.close()
                print(" +   Database connection closed.")

