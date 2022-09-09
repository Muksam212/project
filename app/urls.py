from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

## For image handeling
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index),
    path('index/',views.index),
    path('About/',views.About, name="About"),
    path('contact/',views.contact, name="contact"),
    path('signin/',views.signin,name="signin"),
    path('admindashboard/',
            views.admindashboard,
            name="Admin dashboard"),
    path('customerdashboard/',
            views.customerdashboard,
            name="Customer dashboard"),
    path('signout/',views.signout,name="User Sign Out"),
    path('signup/',views.signup,name="User Sign Up"),
    path('register/', views.registration, name='register'),
    
    path('welcome/', views.welcome, name='welcome'),
    path('profile/', views.profile_user, name='profile'),
    path('profileupdate/', views.profile_update, name='profile_update'),
    path('khaltirequest/',views.khaltireq_view.as_view(), name='khaltirequest'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('movieinfo/', views.movieInfo, name='movieinfo'),
    path('addmovie/', views.addMovie, name='addmovie'),
    path('viewmovie/<int:pk>', views.viewMovie, name='viewmovie'),
    path('deletemovie/<int:pk>', views.deleteMovie, name='deletemovie'),
    path('updatemovie/<int:pk>', views.updateMovie, name='updatemovie'),
    path('seat/', views.seat, name='seat'),
    path('bookedstatus/', views.bookedstatus, name='seat'),
    path('seatbook/<int:pk>', views.bookseat, name='seatbook'),



    
   

    
    
    



    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)