# Generated by Django 3.0.14 on 2022-07-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_seat_customer_seat_movie_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='moviesinformation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
