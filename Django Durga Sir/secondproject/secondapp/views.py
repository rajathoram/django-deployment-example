from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def date_time_view(request):
    s = datetime.datetime.now()
    return HttpResponse('<h1>'+str(s)+'<h1>')
