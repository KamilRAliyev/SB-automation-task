# Task Description

- [x]  REST API to get financial historic data about AAPL stocks
- [x] Store them in Oracle SQL database (I used postgres because digital ocean only provides it and MySQL)
- [x] Fetch csv file to ansible server
- [ ] Generate report from stored data
    - [ ] Amount of stored data
    - [ ] Worst stock day
    - [ ] Best stock day
    - [ ] Draw a chart

--- 

# Workflow
- [x] Basic Server configurations
- [x] Requirements
    - [x] Copy requirements.txt file 
    - [x] Install requirements
- [x] Database configuration
    - [ ] Create new database 
    - [x] Copy config_db.py file to server
    - [x] Create table by running config_db.py
    - [x] Log results
    - [x] Show results
- [x] Application Deployment
    - [x] Unzip tar archive of application to server
    - [ ] Create data module 
        - [x] Seeding with API
        - [ ] Seeding with bulk data
- [x] ApiSeeder class:
    - [x] Store api key in configurations module
    - [x] Implement fetch_data(function) method
    - [x] Store outputs in `/outputs/results`
    - [x] Implement push_to_database method
- [] Cron task for fetching data once in a month
- [] ExtractorDB class
- [] Grafana
- [] Nginx Configuration
---

# Sequence Diagram