# Generated by Django 3.2 on 2021-04-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210416_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imsuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]