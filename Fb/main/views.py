from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import time
from django.contrib import messages

from main.models import UserProfile, UserPost, PostImage
from django.contrib.auth.models import User
from .forms import ChangePasswordForm

# @login_required
def home(request):
    if request.user.is_authenticated:
        # return HttpResponse(f"<h1>hamim ahmed</h1> {user_id}") # using an f-string to format the HTML content and include the user_id
        try:
            user_id = request.session.get('user_id')
            user_post = UserPost.objects.all().order_by('-datetime')    #user_id is the primary & foreignkeu for userpost
            current_user = User.objects.get(id=user_id)
            user_profile = UserProfile.objects.get(user_id=user_id)
            post_images = PostImage.objects.all().order_by('-id')
            # print(user_post,current_user)
        except UserProfile.DoesNotExist:
            # Handle the case where the UserProfile does not exist
            user_post = None
            current_user = None
            messages.success(request,'invalid credentials')
            return redirect('/signin')
            # Create a context dictionary with the objects to pass to the template
        context = {
            'user_post': user_post,
            'post_images': post_images,
            'current_user': current_user,
            'user_profile': user_profile,
            'login_user': current_user,
        }
        for images in post_images:
            print(images)
            print(images.images)


        return render(request, 'home.html', context)
    else:
        # return HttpResponse("<h1>Authentication failed</h1>")
        # time.sleep(2)
        return redirect('/signin')
@login_required()
def profile(request):
    user_id = request.session.get('user_id')

    try:
        user_profile = UserProfile.objects.get(user_id=user_id)
        current_user = User.objects.get(id=user_id)
        user_post = UserPost.objects.filter(user_id=user_id).order_by('-datetime')
        post_images = PostImage.objects.all().order_by('-id')
    except UserProfile.DoesNotExist:
        # Handle the case where the UserProfile does not exist
        user_profile = None
        current_user = None

        # Create a context dictionary with the objects to pass to the template
    context = {
        'user_profile': user_profile,
        'current_user': current_user,
        'user_post': user_post,
        'post_images': post_images,
        'login_user': current_user,
        'login_profile': user_profile,
    }
    # print(user_post)
    # print(user_profile.nick_name)
    # print(current_user,user_id)
    return render(request, 'profile.html', context)
@login_required()
def requested_profile(request):
    requested_user_id = int(request.GET.get('requested_user'))       #terning the value into int as it returns as string.
    login_id = request.session.get('user_id')
    # print(type(requested_user_id) ,type(login_id))
    try:
        requested_user_profile = UserProfile.objects.get(user_id=requested_user_id)
        requested_user = User.objects.get(id=requested_user_id)
        user_post = UserPost.objects.filter(user_id=requested_user_id).order_by('-datetime')
        login_user = User.objects.get(id=login_id)
        login_user_profile = UserProfile.objects.get(user_id=login_id)
    except UserProfile.DoesNotExist:
        # Handle the case where the UserProfile does not exist
        user_profile = None
        current_user = None

        # Create a context dictionary with the objects to pass to the template
    context = {
        'user_profile': requested_user_profile,
        'current_user': requested_user,
        'user_post': user_post,
        'login_user': login_user,
        'login_profile': login_user_profile,
    }
    print(requested_user_id, login_id)
    if requested_user_id == login_id:
        return redirect('/profile')
    else:
        # if requested_user_profile.profile_photo:
        print("photo here:", requested_user_profile.profile_photo)
        print("photo here:", login_user_profile.profile_photo)

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
        profile_photo = request.FILES.get('profile_photo')
        cover_photo = request.FILES.get('cover_photo')
        # print(f_name)
        # print(l_name)
        # print(profile_photo)
    try:
        current_user = User.objects.get(id=user_id)
        user_profile = UserProfile.objects.get(user_id=user_id)   #user_id of user_profile is the onetoone relation with User model

        current_user.first_name = f_name
        current_user.last_name = l_name
        user_profile.nick_name = nick_name
        user_profile.profession = profession
        current_user.email = email
        user_profile.address = address
        if profile_photo:
            user_profile.profile_photo = profile_photo
            # print(profile_photo)
        if cover_photo:
            user_profile.cover_photo = cover_photo

        user_profile.save()
        current_user.save()

        return redirect('main:profile')

    except UserProfile.DoesNotExist:
        # Handle the case where the UserProfile does not exist
        user_profile = None
        current_user = None
    return HttpResponse(f"<h1>info update failed</h1> {f_name}")

def createPost(request):
    user_id = request.session.get('user_id')
    try:
        user_profile = UserProfile.objects.get(user_id=user_id)
        current_user = User.objects.get(id=user_id)
    except UserProfile.DoesNotExist:
        # Handle the case where the UserProfile does not exist
        user_profile = None
        current_user = None
    if request.method == 'POST':
        post = str(request.POST['post'])
        images = request.FILES.getlist('images')
        print(images)

        current_user = User.objects.get(id=user_id)
        user_post = UserPost.objects.create(
            user=current_user,  # Associate the Current_user object with the post as foreignkey
            user_profile=user_profile,
            post=post,
        )
        user_post.save()
        if images:
            # print("from images")
            for image in images:
                PostImage.objects.create(post=user_post, images=image)


        messages.success(request,'Post Created Successfully')
        return redirect('/')

def updatePost(request):
    user_id = request.session.get('user_id')


    if request.method == 'POST':
        updated_post = str(request.POST['edited'])
        post_id = request.POST['post_id']
        op = request.POST['operation']
        view_name = request.POST['view_name']
        referrer = request.META.get('HTTP_REFERER', None)    #from where the post req is coming
        # print(referrer)
        print(op)
    try:
        user_post = UserPost.objects.get(id=post_id)
        current_user = User.objects.get(id=user_id)
    except UserProfile.DoesNotExist:
        # Handle the case where the UserProfile does not exist
        user_profile = None
        current_user = None

    if request.user.is_authenticated:
        if op == "update":
            user_post.post = updated_post
            user_post.save()
        if op == "delete":
            user_post.delete()
        # print(updated_post)
        # print(op)
        print(view_name)
        if view_name == "profile":
            return redirect('/profile')
        return redirect('/')
    else:
        # return HttpResponse("<h1>Authentication failed</h1>")
        # time.sleep(2)
        return redirect('/signin')
def deletePost(request, id):
    print("from deletepost", id)

@login_required
def change_password(request):
    # return render("<h2>from pass change<h2>")
    # return HttpResponse(f"<h2>from pass change<h2>")
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_password = form.cleaned_data['current_password']
            new_password = form.cleaned_data['new_password']
            user = request.user

            # Authenticate the user with the current password
            if authenticate(username=user.username, password=current_password):
                # Update the user's password to the new one
                user.set_password(new_password)
                user.save()
                print("info:", current_password, new_password, user)
                logout(request)
                messages.success(request, 'Password changed successfully.')
                return redirect('/signin')  # Redirect to user's profile page
            else:
                messages.error(request, 'Incorrect info or pass change failed.')
                return redirect('/changepass')
    else:
        form = ChangePasswordForm()
    return render(request, 'profile.html', {'form': form})
@login_required
def user_logout(request):
    # user_id = request.session.get('user_id')
    # return HttpResponse(f"<h1> logout for id <h1> {user_id}")
    logout(request)
    return redirect('/signin')
