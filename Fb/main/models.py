from django.db import models
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    profession = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='cover_photos/', blank=True, null=True)

    # Add other fields for the user profile as needed


    def __str__(self):    #this function display the objects as string names in the admin panel.
        return f"{self.id}, {self.nick_name}, {self.phone}, {self.address},{self.profile_photo},{self.cover_photo}"   # f for displays the actual values

class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts', blank=True, null=True)
    post = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):    #this function display the objects as string names in the admin panel.
        return f"{self.id}, {self.user}, {self.user_profile}, {self.post}, {self.datetime}"   # f for displays the actual values
