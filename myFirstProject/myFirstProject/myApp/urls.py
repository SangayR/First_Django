from django.urls import path
from .templates import views

urlpatterns = [
    path('', views.index),
]