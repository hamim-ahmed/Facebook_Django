from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AppUsers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):    #this function display the objects as string names in the admin panel.
        return f"{self.id} {self.first_name} {self.last_name} {self.phone} {self.joined_date}"   # f for displays the actual values


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     email = models.EmailField(max_length=254, blank=True)
#     address = models.CharField(max_length=255, blank=True)
#     # Add other fields for the user profile as needed
#
#
#     def __str__(self):    #this function display the objects as string names in the admin panel.
#         return f"{self.id} {self.first_name} {self.last_name} {self.email}"   # f for displays the actual values

# def populate_user_profile(sender, instance, **kwargs):
#     if instance.user:
#         instance.first_name = instance.user.first_name
#         instance.last_name = instance.user.last_name
#         instance.email = instance.user.email
#
# # Connect the signal handler function to the pre_save signal
# from django.db.models.signals import pre_save
# # from ..models import UserProfile
#
# pre_save.connect(populate_user_profile, sender=UserProfile)
