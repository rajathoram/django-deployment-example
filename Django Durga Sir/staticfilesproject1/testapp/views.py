import datetime

from django.shortcuts import render

# Create your views here.
def date_time_view(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    if h < 12:
        msg = 'Hello Guest!!! Very Good Morning!!!'
    elif h < 16:
        msg = 'Hello Guest!!! Very Good Afternoon!!!'
    elif h < 16:
        msg = 'Hello Guest!!! Very Good Evening!!!'
    else:
        msg = 'Hello Guest!!! Very Good Night!!!'
    my_dict = {'date': date, 'msg': msg}

    return render(request, 'testapp/results.html', my_dict)

