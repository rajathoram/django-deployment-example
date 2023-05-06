from django.shortcuts import render
import datetime

# Create your views here.
def wish(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = 'Hello Guest !!! Very Good'
    if h < 12:
        msg += 'Morning!!!'
    elif h < 16:
        msg += 'Afternoon!!!'
    elif h < 21:
        msg += 'Evening!!!'
    else:
        msg += 'Night!!!'

    return render(request, 'testapp/results.html', {'msg': msg, 'date':date})
