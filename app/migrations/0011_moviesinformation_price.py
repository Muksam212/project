# Generated by Django 4.0.4 on 2022-06-18 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_movies_moviesinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesinformation',
            name='price',
            field=models.PositiveIntegerField(default=500),
        ),
    ]