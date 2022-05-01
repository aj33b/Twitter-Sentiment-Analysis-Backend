from django.urls import re_path
from twitter_api import views

urlpatterns = [
    re_path('fetch-tweets', views.index),
]
