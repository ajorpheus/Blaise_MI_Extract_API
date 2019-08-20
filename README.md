# Blaise_MI_Extract_API
This is an API to access surveys' Management Information (MI). This resource aims to provide the information required by the Social survey Division MI Hub. 
#### To do
- [ ] Narrow down requirements from MI Hub
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

The following output will be provided for each <serial_number> in the database:
```json
{
  "<serial_number>": {
    "ADDRESS": "<address>", 
    "HHOLD": "<hhold>", 
    "HOUT": "<hout>", 
    "INTNUM": "<intnum>", 
    "NAME": "<name>", 
    "QUOTA": "<quota>"
  }
}
```
Some of the fields are part of the default output. Additional fields can be requested in the MI_spec of each instrument. 

### Development environment

#### Prerequisites
- Install Docker

#### Setup
This setup assumes you're using a local database
1. Clone this project ```git clone https://github.com/ONSdigital/Blaise_Survey_Manager.git```
 
2. Create a .env file and add the settings:
    ```.env
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://{user}:{password}@{hostname}:{port}/{database}'
    SECRET_KEY='{secret_key}'  
    ENV='DEV'  
    ```
    for example: 
    ```.env
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:example@localhost:3306/bsmdb'
    SECRET_KEY='123456'
    ENV='DEV'
    ```
3. Start Docker and run ```docker-compose up -d``` to start the container.
4. If you don't already, get a copy of alembic.ini and the alembic folder in ```https://github.com/ONSdigital/Blaise_Survey_Manager/tree/develop/alembic```. 
    
    Upgrade the database structure ```alembic upgrade head```.
5. Run the application ```flask run```

For the OPN1901 survey, the application should be viewable at ```http://localhost:5000/management_information/opn/2001?api_key=123456```
