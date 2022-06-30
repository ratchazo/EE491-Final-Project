from django.urls import path

from .import views

app_name = 'dafitnessapp'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('calculator', views.IndexView.as_view(), name='index'),
    path('daily-calorie-intake', views.ResultsView.as_view(), name='results'),
    path('new', views.CreateView.as_view(), name='create'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
]
