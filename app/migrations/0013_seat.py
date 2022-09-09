# Generated by Django 4.0.4 on 2022-06-21 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_moviesinformation_choosedate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatno', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='seat')),
                ('totalseat', models.PositiveIntegerField()),
                ('bookstatus', models.CharField(choices=[('Booked', 'Booked'), ('Unbooked', 'Unbooked')], default='Unbooked', max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movie_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.moviesinformation')),
            ],
            options={
                'verbose_name_plural': 'Seat',
            },
        ),
    ]