from django.db import models

# Create your models here.
class AppUsers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):    #this function display the objects as string names in the admin panel.
        return f"{self.id} {self.first_name} {self.last_name} {self.phone} {self.joined_date}"
