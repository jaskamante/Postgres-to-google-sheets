# PostgresSQL to Google Sheets Python Script

## Description and usage

This script connects to a Postgres database and reads the data from a specified table into a specified spreadsheet (by name). It depends on the correct credentials having already been set up and made available in the named files below. All files must be in the same directory.

To call the function in the script, see the example in test_table_to_sheets.py

### Files required (Other than python files)

---

* client_secret.json – the credentials for accessing your Google Drive API (do not check in to GIT)

* config.json – holds the database connection details and the google spreadsheet details (do not check in to GIT)

Note that I have provided dummy files as templates. You can update these and rename them to remove the dummy

### Set up required

---

* Add your db connection details and google spreadsheet details to the config.json file file in the same working directory as the python scripts

* Install the Python libraries by running

```bash
pip install -r requirements.txt
```

* use cli.py or use test_table_to_sheets.py as an example to use it from a python script/project

#### Steps to make Google Configs ready

1. Go to the Google APIs Console.
2. Create a new project.
3. Click Enable API. Search for and enable the Google Drive API.
4. Create credentials for a Web Server to access Application Data.
5. Name the service account and grant it a Project Role of Editor.
6. Download the JSON file.
7. Copy the JSON file to your code directory and rename it to client_secret.json
8. Create a new google sheet with the same name as that specified in your config.py
9. Share the sheet with the email in your client_secret.json

### TODO

---

* [ ] make pypi package
* [ ] make CLI (WIP)
