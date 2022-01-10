# Task Description

- [x]  REST API to get financial historic data about AAPL stocks
- [x] Store them in Oracle SQL database (I used postgres because digital ocean only provides it and MySQL)
- [x] Fetch csv file to ansible server
- [x] Generate report from stored data
    - [x] Amount of stored data
    - [x] Worst stock day
    - [x] Best stock day
    - [x] Draw a chart

--- 

# Workflow
- [x] Basic Server configurations
- [x] Requirements
    - [x] Copy requirements.txt file 
    - [x] Install requirements
- [x] Database configuration
    - [x] Copy config_db.py file to server
    - [x] Create table by running config_db.py
    - [x] Log results
    - [x] Show results
- [x] Application Deployment
    - [x] Unzip tar archive of application to server
    - [x] Create data module 
        - [x] Seeding with API
- [x] ApiSeeder class:
    - [x] Store api key in configurations module
    - [x] Implement fetch_data(function) method
    - [x] Store outputs in `/outputs/results`
    - [x] Implement push_to_database method

---
# How To Run?

| No | Command | Description |
|---|---|---|
| 1. | `git clone https://github.com/KamilRAliyev/swedbank-automation-task.git` | Clone repo |
| 2. | `cd swedbank-automation-task` | Go to project directory |
| 3. | | Configure `./src/configurations/api.py` with API Key |
| 4. | | Configure `./src/configurations/db.py` with DB parameters |
| 4. | | Configure `./ansible_dir/hosts` file with Ubuntu Server |
| 5. | `sh generate_tar.sh` | Generate archive |
| 6. | `cd ansible_dir` | Go to ansible directory |
| 7. | `ansible-playbook -i hosts deploy_application.yml` | Run ansible playbook |

---

# Output Examples:

1. Report: [report.pdf](./examples/report.pdf)
