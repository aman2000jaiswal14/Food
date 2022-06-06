from django.urls import path
from . import views


urlpatterns = [path('recommender_page/',views.recommendation_home,name='recommendation_home'),
               path('recommender_page/get_recommendation',views.get_recommendation,name='get_recommnedation')
               ]
