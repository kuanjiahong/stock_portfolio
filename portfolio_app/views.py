from django.http import HttpRequest
from django.shortcuts import render
from helpers.google_api_helper.read_sheets import get_values, create_dict_from_value_range, SPREADSHEET_ID, RANGE_NAME

def index(request: HttpRequest):
    """Home page of portfolio app"""
    latest_transactions_list = create_dict_from_value_range(get_values(SPREADSHEET_ID, RANGE_NAME))
    context = {'latest_transactions_list': latest_transactions_list}
    return render(request, 'portfolio_app/index.html', context)
