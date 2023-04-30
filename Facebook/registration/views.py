from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def testfunction(request):
    template = loader.get_template("test1.html")
    return HttpResponse(template.render())
    # return HttpResponse("<h1> hello World</h1>")

def signin(request):
    temp = loader.get_template('signin.html')
    return HttpResponse(temp.render())

def signup(request):
    temp = loader.get_template("signup.html")
    return HttpResponse(temp.render())
