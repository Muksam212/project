# Generated by Django 4.0.4 on 2022-06-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_seat_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='totalseat',
            field=models.PositiveIntegerField(blank=b'I01\n', default=0, null=b'I01\n'),
        ),
    ]
