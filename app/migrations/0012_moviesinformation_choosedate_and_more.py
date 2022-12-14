# Generated by Django 4.0.4 on 2022-06-21 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_moviesinformation_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesinformation',
            name='choosedate',
            field=models.DateField(blank=b'I01\n', null=b'I01\n'),
            preserve_default=b'I01\n',
        ),
        migrations.AlterField(
            model_name='moviesinformation',
            name='showtime',
            field=models.CharField(choices=[('Morning(7 to 10am)', 'Morning(7 to 10am)'), ('Afternoon(1 to 3pm)', 'Afternoon(1 to 3pm)'), ('Evening(7 to 9pm)', 'Evening(7 to 9pm)')], default='Morning', max_length=100),
        ),
    ]
