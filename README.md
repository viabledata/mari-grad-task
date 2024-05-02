# mari-grad-task
The task: build a small service that reads an excel file and saves the records to database.​ There are 2 endpoints to be made available: a POST endpoint to load the file into database; a GET endpoint to find person by name and return the information.

## How to currently run the service:
- Clone the repo
- Create a Python virtual environment and activate it (python version 3.9)
```
python -m venv venv
```
```
venv\Scripts\activate
```

- Install the requirements
```
pip install -r requirements.txt
```
- Run the app.py file
  
## How to currently run tests:
- Run the test_read_excel.py file

## If running the service locally, the current endpoint is:
```
http://127.0.0.1:5000/v1/read [POST]
```
