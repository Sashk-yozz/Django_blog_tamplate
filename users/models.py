from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # Поле с сылкой на конкретную запись
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    # Загружает изображение для каждого конкретного пользователя
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')

    # Отображает форматированое имя в профиле
    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    # Проводим проверку размера загруженого фото и обризаем если фото больше чем 256 px
    def save(self, *args, **kwargs):
        super().save()
        image = Image.open(self.img.path)
        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
