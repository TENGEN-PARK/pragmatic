from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_Hello_World = HelloWorld()
        new_Hello_World.text = temp
        new_Hello_World.save()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output' : new_Hello_World})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})
