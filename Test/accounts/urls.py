from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView, name='login'),
    path('signup/', views.SignUpView, name='signup'),
    path('logout/', views.LogOutView, name='logout'),
]