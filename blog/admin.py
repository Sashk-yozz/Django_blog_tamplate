from django.contrib import admin
from .models import News

# Registering table from database for admin panel
admin.site.register(News)
