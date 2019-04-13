# this file shows how to use and call the table_to_sheets function
# you can also just run the python script to test the code and set up like below
# python3 postgres_to_google_sheets

from postgres_to_google_sheets import table_to_sheets
from config import CONFIG_INFO 

# get config info
table_name = format(CONFIG_INFO["table_name"])
sheet_name = format(CONFIG_INFO["sheet_name"])

# call function to transfer data from a table to google sheets
table_to_sheets(table_name, sheet_name)



