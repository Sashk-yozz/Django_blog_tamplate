from django.contrib import admin
from .models import News

# Регестрируем таблицу из БД для Админ панели
admin.site.register(News)
