from decimal import Decimal

from django.http import HttpRequest
from django.shortcuts import render
from django.utils import timezone

from stock_portfolio.financial_modeling_prep_api import get_stock_price
from .models import Portfolio


def index(request: HttpRequest):
    """Home page of portfolio app"""

    today_utc = timezone.now()
    today_isoweekday = today_utc.isoweekday()
    # Monday: 1 - Sunday: 7
    if today_isoweekday == 7:
        stock_price = str(get_stock_price("AAPL")[0]['price'])
        stock_price = Decimal(stock_price)
        total_cost = Decimal(str(stock_price * 1000))
        portfolio = Portfolio(stock_symbol="AAPL", purchased_price=Decimal("162.51"), quantity=1000,
                                  purchased_timestamp=today_utc, total_cost=total_cost)
        portfolio.save()

    latest_transactions_list = Portfolio.objects.order_by('-purchased_timestamp')

    context = {'latest_transactions_list': latest_transactions_list}

    return render(request, 'portfolio_app/index.html', context)
