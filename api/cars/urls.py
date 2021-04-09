from django.contrib import admin
from django.urls import path
from cars.views import *

urlpatterns = [
  path('car/create/', CarCreateView.as_view()),
  path('all/', CarListView.as_view()),
]