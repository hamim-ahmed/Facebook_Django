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
from django.contrib.messages import add_message, get_messages

from main.models import UserProfile
from django.contrib.auth.models import User



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
            # time.sleep(2)
            if user.is_authenticated:  #if logged in
                request.session['user_id'] = user.id         #storing the userid into a session variable(user_id) for further uses
            return redirect('main:home')    #name of redirect app and view name

        else:
            return HttpResponse("<h1> couldn't authenticate<h1>")
    else:
        # temp = loader.get_template('signin.html')
        # return HttpResponse(temp.render())
        return render(request, 'signin.html')

def signup(request):
    # print(UserProfile.objects.all().values())
    # form = CustomUserCreationForm(request.POST)  # creating object for django form with POST data.
    # username = form.cleaned_data['username']
    # print(username)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)      #creating object for django form with POST data.

        if form.is_valid():
            user = form.save()    #saving the User object from signup form

            print("after save")
            new_user = form.cleaned_data['username']
            print(new_user)
            user_instance = User.objects.get(username=new_user)     #also creating user_info object for user_profile model
            user_info = UserProfile.objects.create(
                user=user_instance,
                nick_name="",
                phone="",
                profession="",
                address=""
            )
            user_profile = user_info.save()     #saving the user info in database.

            if user:    #form.save is true/ saved in database
                messages.success(request, 'Registration successful. You can now sign in.')   #this msg will automatically received in the redirected view like session
                return redirect('signin')
            else:
                print("couldn't save")
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()        #creating object from django_custom_form from forms.py.
    return render(request, 'signup.html', {'form': form})
