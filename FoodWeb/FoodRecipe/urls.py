from django.contrib import admin
from django.urls import path

from . import views as classfication_views


urlpatterns = [
    path('index/',classfication_views.index,name='RecipeHomePage'),
    path('recipepage/',classfication_views.recipepage,name='RecipePage1'),
    path('recipepage/showrecipe',classfication_views.showrecipe,name='RecipePage2'),


]