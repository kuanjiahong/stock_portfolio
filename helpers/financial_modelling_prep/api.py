"""A module to interact with Financial Modeling Prep API"""

import os
from typing import List

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FINANCE_MODELING_PREP_API_KEY")
API_ADDRESS = "https://financialmodelingprep.com/api/v3/"


def get_stock_price(stock_symbol: str) -> List[object]:
    """
    Get price of stock

    :param stock_symbol: the stock symbol to buy e.g. AAPL
    :return: [{"symbol": str, "price": number, "volume": number}]
    """

    url = API_ADDRESS + "quote-short/" + stock_symbol + "?apikey=" + API_KEY

    return requests.request("GET", url).json()


if __name__ == "__main__":
    print(get_stock_price("AAPL"))
