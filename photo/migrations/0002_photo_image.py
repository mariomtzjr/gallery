# Generated by Django 2.2 on 2020-03-15 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='gallery/no-img.jpg', upload_to='gallery'),
        ),
    ]
