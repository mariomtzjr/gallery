# Generated by Django 3.0.4 on 2020-03-15 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_auto_20200315_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='photos',
        ),
    ]
