import os
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class CityModel(models.Model):
    class Meta:
        db_table = 'city'

    city = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.city


class OfficeModel(models.Model):
    class Meta:
        db_table = 'office'

    objects = models.Manager()

    name = models.CharField(max_length=30)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10, blank=True,
                             validators=[RegexValidator('^([0])(\d{9})$', 'not valid number')])
    price = models.IntegerField(max_length=20)
    users = models.ManyToManyField(User, related_name='offices')
    photo = models.ImageField(upload_to=os.path.join('office', 'img'),
                              default='https://pngimg.com/uploads/moon/moon_PNG22.png')

    def __str__(self):
        return self.name
