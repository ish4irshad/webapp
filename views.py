from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'webapp/home.html')
    #return HttpResponse("<H2>HEY WELCOME </H2>")


# Create your views here.
