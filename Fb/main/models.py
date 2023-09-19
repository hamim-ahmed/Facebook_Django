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

    # Add other fields for the user profile as needed


    def __str__(self):    #this function display the objects as string names in the admin panel.
        return f"{self.id} {self.nick_name} {self.phone} {self.address}"   # f for displays the actual values

class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):    #this function display the objects as string names in the admin panel.
        return f"{self.id} {self.user} {self.post} {self.datetime}"   # f for displays the actual values
