import random
import re
from django.core.exceptions import ValidationError
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
        blank=True,
        null=True,
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
        blank=True,
        null=True,
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return ' '.join(filter(None, [self.firstname, self.name, self.fathername]))


VALID_LETTERS = 'АВЕКМНОРСТУХ'
class Region(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Введите название региона',
        verbose_name='Название региона',
    )
    number = models.CharField(
        max_length=3,
        help_text='Введите номер региона',
        verbose_name='Номер региона',
    )
    def __str__(self):
        return ' '.join(filter(None, [self.name, self.number]))

class CarNumber(models.Model):
    number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Номер автомобиля',
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.number

    @staticmethod
    def generate_number(region_number):
        while True:
            letter1 = random.choice(VALID_LETTERS)
            digits = f'{random.randint(0, 999):03}'
            letter2 = random.choice(VALID_LETTERS)
            letter3 = random.choice(VALID_LETTERS)
            number = f'{letter1}{digits}{letter2}{letter3}{region_number}'
            if not CarNumber.objects.filter(number=number).exists():
                return number

    def save(self, *args, **kwargs):
        if not self.number:
            self.number = self.generate_number(self.region.number)
        super().save(*args, **kwargs)

    def clean(self):
        pattern = rf'^[{VALID_LETTERS}]\d{{3}}[{VALID_LETTERS}]{{2}}{self.region.number}$'
        if not re.match(pattern, self.number):
            raise ValidationError(f'Номер {self.number} не соответсвует формату для региона {self.region.number}')


