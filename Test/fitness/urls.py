from django.urls import path

from .import views

app_name = 'Da Fitness App'
urlpatterns = [
    path('', views.index, name='index'),
]