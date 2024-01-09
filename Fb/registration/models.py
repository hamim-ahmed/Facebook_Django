from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AppUsers(models.Model):                #currentyly not using in the project....default django User model is used with custom django form.
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):    #this function display the objects as string names in the admin panel.
        return f"{self.id} {self.first_name} {self.last_name} {self.phone} {self.joined_date}"   # f for displays the actual values


