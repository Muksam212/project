from contextvars import Context
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.urls import reverse
from django.views.generic import View 
import smtplib as smtp




from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .form import  UserProfileUpdate, UserupdateForm,UserRegistraationForm, movieform,MovieInformation,Addmovieform,Updatemovieform

# Create your views here.
def index(request):
    return render(request,'index.html')

def signin(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])
            login(request, user)
            print(user.is_superuser)
            if user.is_superuser == True:
                 return redirect('/admindashboard/')
            else:
                return redirect('/customerdashboard/')
    return render(request, 'signin.html', {'form': form})
   

def admindashboard(request):
    movies = Movies.objects.all()
    context = {
        "movies": movies
    }

    return render(request, 'admindashboard.html',context)

def customerdashboard(request):
    movies = Movies.objects.all()
    context = {
        "movies": movies
    }

    return render(request, 'customerdashboard.html',context)




def signout(request):
    logout(request)
    return redirect('/index/')

def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/index/')

    return render(request, 'signup.html',{'form': form}) 
def welcome(request):
    return render(request, 'welcome.html')


def registration(request):

    if request.method == 'POST':
        form = UserRegistraationForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('Done')
            return redirect('login')

    else:
        form = UserRegistraationForm()

    context = {
        'form': form
    }

    return render(request, 'register.html', context)  



    
def profile_user(request):
    return render(request, 'profile.html')

def profile_update(request):
    if request.method == 'POST':
        user_form = UserupdateForm(request.POST, instance=request.user)
        user_profile = UserProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and user_profile.is_valid():
            user_form.save()
            user_profile.save()
            return redirect('/profile/')
    
    else:
        user_form = UserupdateForm(instance=request.user)
        user_profile = UserProfileUpdate(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'user_profile': user_profile
    }
    
    return render(request, 'profileupdate.html', context)

    






def contact(request):
    return render(request, 'contact.html')

def About(request):
    return render(request, 'About.html')

def movieInfo(request):
    if request.method == 'POST':
        movie_form = MovieInformation(request.POST)
        
        if movie_form.is_valid():
            movie_form.save()
            return redirect('/admindashboard/')
    
    else:
        movie_form = MovieInformation()
        
    context = {
        'movie_form': movie_form,
       
    }
    
    return render(request, 'movieinfo.html', context)


def addMovie(request):
    if request.method == 'POST':
        movie_form = Addmovieform(request.POST,request.FILES)
        
        if movie_form.is_valid():
            movie_form.save()
            return redirect('/admindashboard/')
    
    else:
        movie_form = Addmovieform()
        
    context = {
        'movie_form': movie_form,
       
    }
    
    return render(request, 'addmovies.html', context)

def viewMovie(request,pk):
    movie = Movies.objects.get(id=pk)
    movieInfo = MoviesInformation.objects.get(movie=movie)
    
    print(movieInfo)
    if request.method=='POST':
        form = movieform(request.POST)

        if form.is_valid():
            instance=form.save(commit=False)
            instance.movie_name=movieInfo
            form.save()
            return redirect('/Customer dashboard/')
           
    else:
        form = movieform()
        
    
    context = {
        'movie': movie,
        'movieInfo' : movieInfo,
        'form' : form
    }
    
    return render(request, 'viewmovie.html', context)

def deleteMovie(request,pk):
    movie = Movies.objects.get(id=pk)
    movie.delete()
    return redirect('Admin dashboard')

def updateMovie(request,pk):
    movie = Movies.objects.get(id=pk)
    if request.method == 'POST':
        movie_form = Updatemovieform(request.POST,request.FILES,instance=movie)
        
        if movie_form.is_valid():
            movie_form.save()
            return redirect('/admindashboard/')
    
    else:
        movie_form = Updatemovieform(instance=movie)
        
    

    return render(request, 'updatemovie.html', {'movie':movie_form})

def seat(request):
  
    if request.method == 'POST':
        form = movieform(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('Done')
            return redirect('/seatbook')
    else:

        form = movieform()

   
    context = {
        'form': form
    }

    return render(request, 'seat.html', context)  




def bookseat(request,pk):
    seat = Seat.objects.get(id=pk)
    
    if request.method == 'POST':
        if seat.bookstatus == 'Unbooked':
            seat.bookstatus = 'Booked'
            seat.totalseat = seat.totalseat+1
            seat.customer = request.user
            seat.save()
            return redirect('seat')
    else:
        return redirect('seat')
    
    #return render(request, 'seat.html')

def bookedstatus(request):
    status = Seat.objects.all()

    context = {
        'status': status
    }
    return render(request, 'bookedstatus.html',context)

class khaltireq_view(View):
    def get(self,request,*args,**kwargs):
        context = {

        }
        return render(request, 'khaltirequest.html',context)

    
    