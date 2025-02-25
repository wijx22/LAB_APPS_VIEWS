from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('password/generate/', views.generate_password, name='generate_password'),
]
