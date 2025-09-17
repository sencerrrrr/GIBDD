from django.db import models

class Role(models.Model):
    name = models.CharField(
        max_length=30,
        help_text='Введите название роли',
        verbose_name='Название роли',
    )
    description = models.CharField(
        max_length=100,
        help_text='Введите описание роли',
        verbose_name='Описание роли',
    )

    def __str__(self):
        return self.name

class User(models.Model):
    firstname = models.CharField(
        max_length=100,
        help_text='Введите фамилию',
        verbose_name='Фамилия',
    )
    name = models.CharField(
        max_length=100,
        help_text='Введите имя',
        verbose_name='Имя',
    )
    fathername = models.CharField(
        max_length=100,
        help_text='Введите отчество',
        verbose_name='Отчество',
        null=True
    )
