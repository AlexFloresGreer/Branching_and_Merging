from django.shortcuts import render, HttpResponse
from datetime import datetime
import re
from django.http import HttpResponse


#controller
#create views here
# currentYear = now.year
# currentMonth = now.month
# currentDay = now.day
# currentHour = now.hour

def index(request):
    now = datetime.now()
    print now
    data = {
        "timedates": now
    }
    return render(request, "timedisplay/index.html", data)
