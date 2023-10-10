from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    first_name = models.CharField(max_length=50, null=True, default=None, verbose_name="Имя")
    second_name = models.CharField(max_length=50, null=True, default=None, verbose_name="Фамилия")
    date_of_birth = models.DateField(null=True, default=None, verbose_name="Дата рождения")

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f"Пользователь {self.user}: {self.first_name} {self.second_name}"
