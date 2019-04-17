# this file shows how to use and call the table_to_sheets function
# you can also just run the python script to test the code and the set up as below
# python3 postgres_to_google_sheets

from postgres_to_google_sheets import table_to_sheets
from config import config

#google sheets details
config_data = config()
table_name = config_data.get('table_name')
sheet_name = config_data['sheet_name']

# call function to transfer data from a table to google sheets
table_to_sheets(table_name, sheet_name)



