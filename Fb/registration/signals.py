# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import UserProfile
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(
#             user=instance,
#             first_name=instance.first_name,
#             last_name=instance.last_name,
#             email=instance.email
#         )
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()


from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from .models import UserProfile

def populate_user_profile(sender, instance, **kwargs):
    if instance.user:
        instance.first_name = instance.user.first_name
        instance.last_name = instance.user.last_name
        instance.email = instance.user.email

pre_save.connect(populate_user_profile, sender=UserProfile)