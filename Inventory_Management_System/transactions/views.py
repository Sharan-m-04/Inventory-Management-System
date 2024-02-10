from django.shortcuts import render
from django.utils import timezone
import datetime


# Create your views here.
def transactions(request):
    dateTimeNow = datetime.datetime.now()
    dateTimeFormat = dateTimeNow.strftime("%Y-%m-%d, %H:%M")
    return render(request, 'transactions.html', {
        'dateTimeFormat': dateTimeFormat,
    })