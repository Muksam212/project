from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile,MoviesInformation,Movies,Seat


class UserRegistraationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserupdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address']

class MovieInformation(forms.ModelForm):
    startdate = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    enddate = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))

    
    class Meta:
        model = MoviesInformation
        fields = '__all__'

class Addmovieform(forms.ModelForm):

    
    class Meta:
        model = Movies
        fields = '__all__'

class Updatemovieform(forms.ModelForm):

    
    class Meta:
        model = Movies
        fields = '__all__'




class movieform(forms.ModelForm):
    
    class Meta:
        model = Seat
        fields = ['email','contact','no_of_seats']






