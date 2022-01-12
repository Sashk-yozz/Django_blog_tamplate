from django.contrib.auth.models import User
from .models import Profile
# Tracks saving to the database
from django.db.models.signals import post_save
# Adds an action handler to the method
from django.dispatch import receiver


# Tracking the action associated with the User table, call the function
# sander - get the table with which we interact
# instance - get the object that is being registered (instance can be replaced with user)
# created - registration state
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Updates user information
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()