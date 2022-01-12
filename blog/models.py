from django.db import models
# import of current time
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Table in the database named News
class News(models.Model):
    # Fields in table
    # Accepts a small text 255 characters (unique=True: not allow creating with the same names)
    title = models.CharField('Название статьи', max_length=100, unique=True)

    # Can accept unlimited number of characters
    text = models.TextField('Основной текст статьи')

    # Date and time setting field
    date = models.DateTimeField('Дата', default=timezone.now)

    # Author field, (on_delete: when deleting a user, all articles are deleted)
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    # Number of views field
    views = models.IntegerField('Просмотры', default=1)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    # The magic method for changing the title of an article in the database
    def __str__(self):
        return f'{self.title}'

    # Class that renames the name of the table in the admin panel
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
