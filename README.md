PostgresSQL to Google Sheets Python Script

Description and usage:

This script connects to a Postgres database and reads the data from a specified table into a specified spreadsheet (by name). It depends on the correct credentials having already been set up and made available in the named files below. All files must be in the same directory. 

To call the function in the script, see the example in test_table_to_sheets.py

Files required:

	Note that the cofig and credentials files have been checked in as dummies. You will need to edit these with the correct details and change their names to match those below. Also replace the dummy client_secret.json file with your actual client_secret.json file. Make sure all files are in the same directory, or alter the code to cope with alternative file organization. 

postgres_to_google_sheets.py

connection.py - parses and returns the database connection details

test_table_to_sheets.py – shows example usage as defined in the spec

config.py – holds the table name, google sheet name and credential file name

client_secret.json – the credentials for accessing your Google Drive API (do not check in to GIT)

database.ini – holds the database connection details (do not check in to GIT)

Set up required:

•	Add your db connection details to a database.ini file in the same working directory as the python scripts

•	Install the Python libraries below
	
•	Google Sheets API 
1.	Go to the Google APIs Console.
2.	Create a new project.
3.	Click Enable API. Search for and enable the Google Drive API.
4.	Create credentials for a Web Server to access Application Data. 
5.	Name the service account and grant it a Project Role of Editor.
6.	Download the JSON file.
7.	Copy the JSON file to your code directory and rename it to client_secret.json
8.	Create a new google sheet with the same name as that specified in your config.py
9.	Share the sheet with the email in your client_secret.json

Python Libraries:

psycopg2
pandas
pygsheets
