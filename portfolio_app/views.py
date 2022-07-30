from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest):
    """Home page of portfolio app"""

    return HttpResponse("Hello, world. You're at the portfolio index.")
