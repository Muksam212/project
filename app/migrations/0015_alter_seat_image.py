# Generated by Django 4.0.4 on 2022-06-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_seat_customer_remove_seat_movie_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='image',
            field=models.ImageField(default='seat.jpg', upload_to='seat'),
        ),
    ]