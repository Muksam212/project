from django.contrib import admin
from .models import Profile,Movies,MoviesInformation,Seat


# Register your models here.

admin.site.register(Profile)
admin.site.register(Movies)
admin.site.register(MoviesInformation)
admin.site.register(Seat)
