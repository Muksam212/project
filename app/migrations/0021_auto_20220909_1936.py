# Generated by Django 3.0.14 on 2022-09-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20220909_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='showdate',
            field=models.DateField(blank=b'I01\n', default=0, null=b'I01\n'),
        ),
    ]