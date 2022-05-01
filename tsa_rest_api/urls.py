from django.urls import re_path
from tsa_rest_api import views

urlpatterns = [
    re_path('classified-tweets', views.index),
    re_path('classified-tweets/<int:id>', views.index),
]
