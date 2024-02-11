from django.shortcuts import render
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def transactions(request):
    dateTimeNow = datetime.datetime.now()
    dateTimeFormat = dateTimeNow.strftime("%Y-%m-%d, %H:%M")
    return render(request, 'transactions.html', {
        'dateTimeFormat': dateTimeFormat,
    })