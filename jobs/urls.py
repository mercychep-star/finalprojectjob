from django.urls import path
from jobs.views import *
urlpatterns = [
    path('',HomeView.as_view(),name = "home")
]