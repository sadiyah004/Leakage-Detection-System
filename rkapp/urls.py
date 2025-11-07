from django.urls import path
from . import views
urlpatterns = [
    path('register', views.register, name="registerpage"),
    path('fetchdata',views.fetchdata,name="fetchdata"),
    path('water', views.water, name="waterpage"),
    path('',views.login, name="lp"),
    path('ftd',views.ftd,name="fetchdata"),
    path('index',views.dashboard,name = "Dashboard"),
    path('logout',views.logout, name="lop"),
    path('smoke', views.smoke, name="smoke"),
    path('gas', views.gas, name="gas"),
    path('profile', views.profile, name="profile"),
    path('help', views.help, name="hd"),
    path('feedback', views.fb, name="fb"),
    path('pds', views.profiledata, name="profiledatasubmit"),
    path('about', views.about, name="about"),
]
