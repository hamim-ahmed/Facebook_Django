from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import  csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import time
from django.contrib import messages
from .forms import CustomUserCreationForm



# @login_required
def testfunction(request):
    user_id = request.session.get('user_id')      #getting sessoin id set at loggin time.
    # user_name = request.GET.get('name')
    # template = loader.get_template("test1.html")
    # return HttpResponse(template.render(user_name,request))
    # return HttpResponse({{user_name}})
    return HttpResponse(user_id)



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            var = "hamimahmed"
            login(request, user)
            user = request.user      #getting the current logged in user
            print(user)
            time.sleep(2)
            if user.is_authenticated:  #if logged in
                request.session['user_id'] = user.id         #storing the userid into a session variable(user_id) for further uses
            return redirect('testfunction')

        else:
            return HttpResponse("<h1> couldn't authenticate<h1>")

    temp = loader.get_template('signin.html')
    return HttpResponse(temp.render())

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)      #creating object for django form with POST data.
        if form.is_valid():
            user = form.save()
            print("after safe")
            if user:    #form.save is true/ saved in database
                return redirect('signin')
            else:
                print("couldn't save")
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()        #creating object from django_custom_form from forms.py.
    return render(request, 'signup.html', {'form': form})
