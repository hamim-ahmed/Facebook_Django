from django.contrib import admin


# Register your models here.

from .models import AppUsers
admin.site.register(AppUsers)         #registering the AppUsers Model(database table)>>>>for displaying the info. in the admin panel as a table.

# from .models import UserProfile
# admin.site.register(UserProfile)