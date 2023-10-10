from django.db import models
from django.contrib.auth.models import User
from transliterate import translit
from django.utils.text import slugify
from reggg.models import Profile
from PIL import Image


# Create your models here.


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Связанный профиль", related_name="profile")
    title = models.CharField(max_length=100, null=False, verbose_name="Заголовок")
    description = models.TextField(blank=False, null=False, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования")
    slug = models.SlugField(max_length=100, null=False, verbose_name="СЛАГ", blank=False)


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(self.title, 'ru', reversed=True))
        super().save(*args, **kwargs)


class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Связанный профиль")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Связанная новость", related_name="comments")
    text = models.TextField(blank=False, null=False, verbose_name="Текст комментария")

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text

class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', blank=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def save(self, *args, **kwargs):
        if self.image:
            image = Image.open(self.images.path)
            desired_width = 800
            desired_height = 600
            image.thumbnail((desired_width, desired_height))
            image.save(self.images.path)

        super().save(*args, **kwargs)