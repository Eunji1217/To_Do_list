from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.start),
    path('login/', views.login),
]