"""A module to read google sheets"""
from typing import List

from auth import spreadsheet_service
from googleapiclient.errors import HttpError
import os
from dotenv import load_dotenv

load_dotenv()

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
RANGE_NAME = "Transactions!A:E"


def get_values(spreadsheet_id: str, range_name: str) -> List:
    """
    Get the values in a Google Sheet based on the range name given

    :param spreadsheet_id: the spreadsheet id of the Google sheet
    :param range_name: the range in A1 notation
    :return: the values[] field in the ValueRange object
    """
    try:
        result = spreadsheet_service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_name).execute()
        rows = result.get('values', [])
        print(f'{len(rows)} rows retrieved including header')
        return rows
    except HttpError as error:
        print(f'An error occured: {error}')
        return error


def create_dict_from_value_range(values: List) -> List[dict]:
    """
    Create a list of dict from the values[] field in ValueRange object
    received from Google Sheets API

    :param values: the values[] field in ValueRange object
    :return: a list of dictionary with the header row as key
    """
    # the header row as keys
    keys = values[0]
    dict_template = {}
    list_of_dict = []
    # Skipped the header row and start looping the rest of the data
    for i in range(1, len(values)):
        for j in range(len(keys)):
            dict_template[keys[j]] = values[i][j]
        list_of_dict.append(dict_template)
        dict_template = {}
    return list_of_dict


if __name__ == "__main__":
    print(create_dict_from_value_range(get_values(SPREADSHEET_ID, RANGE_NAME)))
    print("Done")
