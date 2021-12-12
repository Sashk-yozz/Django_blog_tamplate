from django.db import models
# Импорт текущего времени
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Таблица в БД с именем News
class News(models.Model):
    # Поля в таблице
    # Принимает не большой текст 255 символов (unique=True не дает создать с одинаковыми названиями)
    title = models.CharField('Название статьи', max_length=100, unique=True)

    # Может принимать не ограничиное кол.символов
    text = models.TextField('Основной текст статьи')

    # Поле установки даты и времени
    date = models.DateTimeField('Дата', default=timezone.now)

    # Поле автора при удалении пользователя удаляються все статьи
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    # Поле количества росмотров
    views = models.IntegerField('Просмотры', default=1)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    # Магичиский метод для изминение название статьи в БД
    def __str__(self):
        return f'{self.title}'

    # Класс который переименовует название таблицы в админ панели
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
