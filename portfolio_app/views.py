from django.http import HttpRequest
from django.shortcuts import render

from .models import Portfolio


def index(request: HttpRequest):
    """Home page of portfolio app"""

    latest_transactions_list = Portfolio.objects.order_by('-purchased_timestamp')

    context = {'latest_transactions_list': latest_transactions_list}

    return render(request, 'portfolio_app/index.html', context)
