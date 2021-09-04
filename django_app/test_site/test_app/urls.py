# Self added codes.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('character_classifier', views.character_classifier,
         name='Character_Classifier'),
]
