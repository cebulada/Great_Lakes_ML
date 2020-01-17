## Great_Lakes_ML

## Authors

- [Daniel Adam Cebula](https://github.com/cebulada)
- [Rohan Chaudhari](https://github.com/focusrohan)
___

## FIRST STEP:  How to setup local posgreSQL database using pgAdmin 4

### 1. Open pgAdmin 4 Software
### 2. Login using your credentials in PostgreSQL 11 server group
### 3. Create a Database called "Great_Lake_ML" (One can use the following SQL code)
```
CREATE DATABASE Great_Lake_ML
    WITH 
    OWNER = <your_name_here>
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;
```
### 4. Run the following [SQL queries](./PostgreSQL_Database/schema.sql) to create the necessary tables
### 5. Done
___

## SECOND STEP:  Load the local postgreSQL database using SQLAlchemy and pandas.to_query()

### 1. Once the Great_Lake_ML database and tables have been created open up jupyter notebook by the following code
```
$ jupyter notebook
```
### 2. Open [water_load_ETL](./Jupyter_Notebooks/water_load_ETL.ipynb) jupyter notebook
### 3. Run all code cells
NOTE: Make sure you include a config folder with postgres python file with your username and password variables
### 4. Done
___

## THIRD STEP:  Start a local Flask server for the API

### 1. Start by going to the location of [app.py](./Flask_Server/app.py) in the file directory
NOTE: Make sure you include a config folder with postgres python file with your username and password variables
### 2. Through terminal line commands start the Flask server
```
$ python app.py
```
### 3. Flask server will be hosted on https://localhost:5000/
### 4. Done
___

## FOURTH STEP:  Start a local python server for the data visualization

### 1. Start by going to the location of [index.html](./Website/index.html) in the file directory
### 2. Through terminal line commands start the Python server
```
$ python -m http.server
```
### 3. Python server will be hosted on https://localhost:8000/
### 4. Done
___