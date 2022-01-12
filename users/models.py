from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # Field with a link to a specific record
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    # Loads an image for each specific user
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')

    # Displays the formatted name in the profile
    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    # Checking the size of the uploaded photo
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
