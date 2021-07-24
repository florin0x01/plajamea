from django.http import HttpResponse
from django.shortcuts import (render, redirect)
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden, FileResponse)
import urllib.request
from urllib.error import *
from . import models
from .common import weather

def numeplaja(request, numeplaja):
    return HttpResponse(f'Hello, world. You\'re at {numeplaja}')

def show_userhome(request):
    request.session['count'] += 1
    return render(request, 'plajamea/userhome.html', {
        'username': request.session['username'],
        'count': request.session['count']
    })

def index(request):
    isLoggedIn = False
    username = ''
    weather_controller = None
    temp_data = {
        'temp': '',
        'co': ''
    }
    if 'username' in request.session:
        isLoggedIn = True
        username = request.session['username']
        weather_controller = weather.WeatherController('ccd2a96c109e4971a9c153205212407')
        temp_data = weather_controller.get_temp_for_city('Bucharest')
        print (temp_data)

    print ("IsLoggedIn: ", isLoggedIn)
    print ("Username: ", username)
    return render(
        request,
        'plajamea/index.html',
        {
            'isLoggedIn': isLoggedIn,
            'username': username,
            'city': 'Bucharest',
            'temp_c': temp_data['temp'],
            'co': temp_data['co']
        }
    )

def login(request):
    if request.method != 'POST':
        return HttpResponseBadRequest('Method should be POST')
    if 'username' in request.session:
        return redirect('/userhome')

    username = request.POST['username']
    results = models.Product.objects.filter(name=username)
    print ("RESULTS", results)
    if len(results) > 0:
        print (results)
        request.session['username'] = username
        request.session['count'] = 0
        return HttpResponse(f'Welcome {username}')
    return HttpResponseForbidden('Username not found',)

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def sendMenu(request):
    url = 'https://www.1pdffiller.com/preview/100/269/100269347/large.png'
    try :
        resp = urllib.request.urlopen(url)
        x = resp.read()
        print(x)
        response = FileResponse(resp.read())
    except URLError as he:
        return HttpResponse("Could not get URL ", he.reason)


    #img = open('/tmp/menu.png', 'rb')
    #response = FileResponse(img)

    return response

