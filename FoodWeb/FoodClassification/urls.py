from django.contrib import admin
from django.urls import path

from . import views as classfication_views


urlpatterns = [
    path('index/',classfication_views.index,name='clasificationHomePage'),
    path('uploadimagepage/',classfication_views.uploadimagepage,name='uploadImage'),
    path('uploadimagepage/uploadedimage', classfication_views.uploadedimage, name='uploadedimage'),

]