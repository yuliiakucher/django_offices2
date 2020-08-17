# Generated by Django 3.1 on 2020-08-17 10:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='officemodel',
            name='users',
            field=models.ManyToManyField(related_name='offices', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='officemodel',
            name='phone',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator('^([0])(\\d{9})$', 'not valid number')]),
        ),
    ]