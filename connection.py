import json

with open('config.json') as config_file:
    data = json.load(config_file)

# database connection details


def connection():

    db = {'host': data['postgres']['host'], 'port': data['postgres']['port'], 'database': data['postgres']['database'],
          'user': data['postgres']['user'], 'password': data['postgres']['password']}
    #print(db)
    return db
