# Blaise_MI_Extract_API
This is an API to access surveys' Management Information (MI). This resource aims to provide the information required by the Social survey Division MI Hub. 
#### To do
- [ ] Figure out why ```Flask run``` does not work
- [ ] Narrow down requirements from MI Hub (Serial number or Case ID?)
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

The following output will be provided for each <primary_key> in the database:
```json
[
  {
    "tla": "<tla>", 
    "field_period": "<field_period>", 
    "primary_key": "<primary_key>", 
    "<MI Spec fields>": "<Response values>",
  }
]
```
Some of the fields are part of the default output. Additional fields can be requested in the MI_spec of each instrument. 

### Development environment

#### Prerequisites
- Install Docker


#### Setup
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
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://{user}:{password}@{hostname}:{port}/{database}'
    SECRET_KEY='{secret_key}'  
    ENV='DEV'  
    ```
    for example: 
    ```.env
    SQLALCHEMY_DATABASE_URI='mssql+pymssql://sa:example123!@localhost:1433/bsmdb'
    SECRET_KEY='123456'
    ENV='DEV'
    ```
5. Setup the developer database using the developer services project.
7. USe a sql management tool to add an api_key to the data base 'api_key' table 
8. Run the application ```flask run``` - This does not work for me; instead I use PyCharm using a configuration where:
    ```text
    Module name: flask
    Parameters: run
    Working directory: <path-to-folder>\Blaise_MI_Extract_API
    ```
    Make sure that the python interpreter is the one from the venv from step 2. 
9. Navigate to the URL. For example, for the OPN1901 survey, the application should be viewable at http://localhost:5000/management_information/opn/2001?api_key=123456


