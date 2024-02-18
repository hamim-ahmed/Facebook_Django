from django.contrib import admin

# Register your models here.

from .models import UserProfile
# admin.site.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):    #this admin class will show database as tabular formate.
    list_display = ('id', 'nick_name', 'phone', 'address', 'profile_photo', 'cover_photo')  # Define which fields to display in the table
    list_display_links = ('id', 'nick_name')  # Define which fields should be linked to the detail view
admin.site.register(UserProfile, UserProfileAdmin)

from .models import UserPost
# admin.site.register(UserPost)
class UserPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_profile', 'post', 'datetime')
    list_display_links = ('id', 'post')  # You can choose which fields to link to the detail view
admin.site.register(UserPost, UserPostAdmin)

from .models import PostImage
# admin.site.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'images')
    list_display_links = ('id', 'images')  # You can choose which fields to link to the detail view
admin.site.register(PostImage, PostImageAdmin)