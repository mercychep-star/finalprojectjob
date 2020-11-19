from django.urls import  path
from users.views import *
app_name = "users"
urlpatterns = [
    path('register/',UserRegisterView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('update-profile/<int:pk>/', UserUpdateView.as_view(), name='update_profile'),

]
