from django.contrib import admin

# Register your models here.
from .models import UserProfile
admin.site.register(UserProfile)

from .models import UserPost
admin.site.register(UserPost)

from .models import PostImage
admin.site.register(PostImage)