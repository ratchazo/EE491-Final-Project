from django.urls import path

from .import views

app_name = 'fitness'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('calculator', views.IndexView.as_view(), name='index'),
    path('daily-calorie-intake', views.ResultsView.as_view(), name='results'),
]
