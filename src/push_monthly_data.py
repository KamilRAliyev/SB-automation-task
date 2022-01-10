from configurations.db import DATABASE_CONFIGS
from configurations.api import API_KEY

from data_management.seed_api import ApiSeeder as seeder

if __name__ == "__main__":
    instance = seeder(API_KEY, DATABASE_CONFIGS, 'AAPL', 'json')
    instance.fetch_data("TIME_SERIES_MONTHLY")
    instance._output_json()
    instance._generate_values()
    instance.push_to_database()