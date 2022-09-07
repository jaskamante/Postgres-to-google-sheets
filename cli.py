import click
from config import config
from postgres_to_google_sheets import table_to_sheets

config_data = config()


@click.command()
@click.option("--query", help="Query to run.", prompt="Enter query")
@click.option("--sheet-name", prompt="Sheet name", default=config_data['sheet_name'],
              help="The key of a spreadsheet. (can be found in the sheet URL)")
def send_to_sheets(query: str, sheet_name: str = config_data['sheet_name']):
    table_to_sheets(query, sheet_name)


if __name__ == '__main__':
    send_to_sheets()
