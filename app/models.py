from itertools import count
from pickle import TRUE
from secrets import choice
from django.db.models import Sum, F
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    image = models.ImageField(default='default.jpg', upload_to = 'Profile_Pic')

    class Meta:
        verbose_name_plural = 'Profile'


    def __str__(self):
        return f'{self.customer.username} profile'

class Movies(models.Model):
    moviename = models.CharField(max_length=100, null=True )
    moviedescription = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to = 'movies')

    class Meta:
        verbose_name_plural = 'Movies'


    def __str__(self):
        return self.moviename


SHOWTIME =(
    ('Morning(7 to 10am)', 'Morning(7 to 10am)'),
    ('Afternoon(1 to 3pm)', 'Afternoon(1 to 3pm)'),
    ('Evening(7 to 9pm)', 'Evening(7 to 9pm)'),
    
)

class MoviesInformation(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()
    showtime = models.CharField(max_length=100, choices=SHOWTIME, default='Morning')
    price = models.PositiveIntegerField(default=500)

    class Meta:
        verbose_name_plural = 'MoviesInformation'


    def __str__(self):
        return self.movie.moviename


    

class Seat(models.Model):
    movie_name = models.ForeignKey(MoviesInformation,on_delete=models.CASCADE, blank=TRUE, null=TRUE)
    email = models.EmailField(blank=TRUE, null=TRUE) 
    contact = models.CharField(max_length=100)
    no_of_seats = models.PositiveIntegerField(blank=TRUE,max_length=100,null=TRUE)
    #show_date = models.DateField(auto_now_add=False)

    
    class Meta:
        verbose_name_plural = 'Seat'

    def get_total_price(self):
        return self.movie_name.price * self.no_of_seats
        
    def __str__(self):
        return self.email

    

    