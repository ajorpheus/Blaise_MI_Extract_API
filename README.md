# Blaise_MI_Extract_API
API to access surveys' Management Information.
#### To do
- [ ] Provide IP address
- [ ] Determine how to provide API key

#### Using the API
To access the management information for a specific survey, go to: 
```
   http://<IP_address>/management_information/<Survey_TLA>/<Field_Period>?api_key=<API_key>
```
You will need to specified the fields in <b>< ></b>; they are described in the following table:

| Field | Description | Examples
|-------|-------------|--------
| Survey_TLA | Three letter acronym for the survey | OPN, LFS |
| Field_Period | Format yymm - Year and month when the survey was carried out| 2001 (January 2020) |
| API_key | Key to be able to access records.

The following output will be provided for each <serial_number> in the database matching request:
```json
{
  <serial_number>: {
    "ADDRESS": <address>, 
    "HHOLD": <hhold>, 
    "HOUT": <hout>, 
    "INTNUM": <intnum>, 
    "NAME": <name>, 
    "QUOTA": <quota>
  }
}
```
