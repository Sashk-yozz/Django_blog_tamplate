# Generated by Django 3.2.9 on 2021-11-15 18:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
    ]
