Bank Branches API

Overview: 
This project is a Django-based REST API that allows users to retrieve information about banks and their branches in India. The API provides endpoints to get a list of banks and detailed branch information based on the IFSC code.

Features: 
1. Bank List: Retrieve a list of all banks.
2. Branch Details: Retrieve details of a specific branch using its IFSC code.

Technologies Used: 
1. Python 3.10.4
2. Django 5.1
3. Django REST Framework
4. PostgreSQL

Setup Instructions:
1. Clone the repository
2. Create and Activate a Virtual Environment

Set Up the Database:
1. PostgreSQL should be installed
2. Create a database for the project: 
   CREATE DATABASE bank_branches;
3. Updated the address column form char(195) to char(255) in the branches table

Apply Migrations: python manage.py migrate

Load Initial Data: 
1. Load the bank branches data from the provided CSV file: Load the bank branches data from the provided CSV file:

Run the Development Server: python manage.py runserver

API Endpoints:
1. List All Banks:
    1. URL: http://127.0.0.1:8000/api/banks/
    2. Method: GET
    3. Description: Retrieves a list of all banks

2. Retrieve Branch Details by IFSC Code:
    1. URL:http://127.0.0.1:8000/api/branches/(ifsc)/
    2. Method: GET
    3. Description: Retrieves detailed information about a specific branch using its IFSC code
    4. Example: URL: http://127.0.0.1:8000/api/branches/HDFC0000053/
    5. Response:
       {
          "ifsc": "HDFC0000053",
          "bank": {
              "bank_id": 5,
              "name": "HDFC BANK"
          },
          "branch": "BANGALORE - KORAMANGALAM",
          "address": "NO.9, ETERNAKORAMANGLA INDUSTRIAL LAYOUTKORAMANGLABANGALOREKARNATAKA560095",
          "city": "BANGALORE",
          "district": "BANGALORE URBAN",
          "state": "KARNATAKA"
       }

Run Unit Tests: python manage.py test
