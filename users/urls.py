from django.urls import  path
from users.views import *
app_name = "users"
urlpatterns = [
    path('register/',UserRegisterView.as_view(), name='register')
]
