from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import time

from main.models import UserProfile, UserPost
from django.contrib.auth.models import User


# @login_required
def home(request):
    user_id = request.session.get('user_id')
    # return HttpResponse(f"<h1>hamim ahmed</h1> {user_id}") # using an f-string to format the HTML content and include the user_id
    if request.user.is_authenticated:
        return render(request, template_name='home.html')
    else:
        # return HttpResponse("<h1>Authentication failed</h1>")
        time.sleep(2)
        return redirect('/signin')
@login_required()
def profile(request):
    user_id = request.session.get('user_id')
    try:
        user_profile = UserProfile.objects.get(user_id=user_id)
        current_user = User.objects.get(id=user_id)
    except UserProfile.DoesNotExist:
        # Handle the case where the UserProfile does not exist
        user_profile = None
        current_user = None

        # Create a context dictionary with the objects to pass to the template
    context = {
        'user_profile': user_profile,
        'current_user': current_user,
    }
    # print(user_profile.nick_name)
    # print(current_user,user_id)
    return render(request, 'profile.html', context)

def updateinfo(request):
    user_id = request.session.get('user_id')
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        nick_name = request.POST['nick_name']
        profession = request.POST['profession']
        email = request.POST['email']
        address = request.POST['address']
        print(f_name)
        print(l_name)
    try:
        current_user = User.objects.get(id=user_id)
        user_profile = UserProfile.objects.get(user_id=user_id)   #user_id of user_profile is the onetoone relation with User model

        current_user.first_name = f_name
        current_user.last_name = l_name
        user_profile.nick_name = nick_name
        user_profile.profession = profession
        current_user.email = email
        user_profile.address = address
        user_profile.save()
        current_user.save()

        return redirect('main:profile')
    except UserProfile.DoesNotExist:
        # Handle the case where the UserProfile does not exist
        user_profile = None
        current_user = None
    return HttpResponse(f"<h1>info update failed</h1> {f_name}")


@login_required
def user_logout(request):
    # user_id = request.session.get('user_id')
    # return HttpResponse(f"<h1> logout for id <h1> {user_id}")
    logout(request)
    return redirect('/signin')
