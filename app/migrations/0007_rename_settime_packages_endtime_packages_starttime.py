# Generated by Django 4.0.4 on 2022-06-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_appointment_noofticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packages',
            old_name='settime',
            new_name='endtime',
        ),
        migrations.AddField(
            model_name='packages',
            name='starttime',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
