# Blaise_MI_Extract_API
This is an API to access surveys' Management Information (MI). This resource aims to provide the information required by the Social survey Division MI Hub. 
#### To do
- [ ] Figure out why ```flask run``` does not work
- [X] Narrow down requirements from MI Hub (Serial number or Case ID?): agreed to use Primary Key (int)
- [ ] Provide IP address
- [ ] Determine how to provide API key

### Using the API
To access the MI for a specific survey, go to: 
```
   http://<IP_address>/management_information/<Survey_TLA>/<Field_Period>?api_key=<API_key>
```
You will need to specified the fields in <b>< ></b> as described in the following table:

| Field | Description | Examples
|-------|-------------|--------
| Survey_TLA | Three letter acronym for the survey | OPN, LFS |
| Field_Period | Format yymm - Year and month when the survey was carried out| 2001 (January 2020) |
| API_key | Key to be able to access records.

The following default output will be provided for each <primary_key> in the database:
```json
{
  "<primary_key>": {
    "ADDRESS": "<address>", 
    "HHOLD": "<hhold>",  
    "INTNUM": "<intnum>", 
    "QUOTA": "<quota>"
  }
}
```
Additional fields can be requested in the MI_spec of each instrument (via the Blaise Survey Manager Website). 

### Development environment

#### Prerequisites
- Install Docker.
- Install HeidiSQL, SSMS or any other administration tool with MS SQL support. 

#### Setup (Docker)
1. Set up the backing services by cloning the repository https://github.com/ONSdigital/Blaise_Developer_Services
and following the setup instructions. This will setup containers for the different services, including one for this API. 
Ensure you have an empty database called 'bsmdb'. You can do this using HeidiSQL.

2. Add the API_key to the bsm.api_key table in your database.
3. Navigate to the URL. For example, for the OPN1901 survey, the application should be viewable at http://localhost:5001/management_information/opn/2001?api_key=123456

##### Having issues?
- If your database is empty, you can upload sample data Blaise Survey Manager: http://localhost:5000
- To debug the API, first stop the container: ```docker-compose stop bmie```;
 then you should be able to run the website in your IDE.
- When restarting the database container, you might need to close and reopen HeidiSQL.



#### Setup (manual)
This setup assumes you're using a local database
1. Clone this project ```git clone https://github.com/ONSdigital/Blaise_MI_Extract_API.git```

2. Create and activate a Python virtual environment and install the requirements: 
    ```
    python -m venv venv 
    venv\scripts\activate
    ```

3. Install the requirements
    ```.env
    pip install -r requirements.txt
    ```
 
4. Create a .env file and add the settings:
    ```.env
    SQLALCHEMY_DATABASE_URI='mssql+pyodbc://{user}:{password}@{hostname}:{port}/{database}'
    SECRET_KEY='{Your_secret_key}'  
    ENV='DEV'  
    ```
    for example: 
    ```.env
    SQLALCHEMY_DATABASE_URI='mssql+pyodbc://sa:example123!@127.0.0.1:1433/bsmdb?driver=ODBC+Driver+17+for+SQL+Server'
    SECRET_KEY='123456'
    ENV='DEV'
    ```
   Make sure these settings match the docker-compose.yml
5. Start Docker and run ```docker-compose up -d```
6. Create an empty database called 'bsmdb'. In HeidiSQL you can use the following settings:

    ![picture](settings_templates/img/bsmdb_HeidiSQL.PNG)

    The containers from step 5 should be able to see this database and update the the database structure. 
    If you do not have any test data on your database, you can upload cases through Blaise Survey Manager.
7. Add the API_key to the bsm.api_key table in your database. 
8. Run the application - I use PyCharm using a configuration where:
    ```text
    Module name: flask
    Parameters: run
    Working directory: <path-to-folder>\Blaise_MI_Extract_API
    ```
    Make sure that the python interpreter is the one from the venv from step 2. 
9. Navigate to the URL. For example, for the OPN1901 survey, the application should be viewable at http://localhost:5000/management_information/opn/2001?api_key=123456


