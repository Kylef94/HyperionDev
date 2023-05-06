from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('tindog', views.tindog),
    path('site', views.personal)
]