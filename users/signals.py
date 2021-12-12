# Отслеживает действие в нутри проекта
from django.contrib.auth.models import User
from .models import Profile
# Отслеживает сохранение в БД
from django.db.models.signals import post_save
# Добавляет к методу оброботчик действия
from django.dispatch import receiver


# Отслеживаем действие связаное с таблицей User, вызываем функцию
# sander - получаем таблицу с которой взаимодействуем
# instance - получаем обьект который регистрируется (instance можно заменить на user)
# created - состояние регистрации
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Обновляет информацию про пользователя
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()