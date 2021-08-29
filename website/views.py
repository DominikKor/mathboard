import json

from django.http import HttpResponse
from django.shortcuts import render

from website.math import Number


def home(request):
    return render(request, "home.html")


def number_dashboard(request, number):
    # Limits the maximum number to 10 million. Numbers over 10 million take too long to process. 
    if number <= 10_000_000:
        num = Number(number)
        response = num.__dict__
    else:
        response = {"message": "Too large number. Must be lower than 10,000,000 (TEN MILLION)"}
    return HttpResponse(json.dumps(response))
