from django.views import generic
from django.urls import reverse_lazy
from .models import dafitnessapp


class HomeView(generic.ListView):
    template_name = 'dafitnessapp/home.html'
    context_object_name = 'dafitnessapp_list'

    def get_queryset(self):
        """Return the all greetings."""
        return dafitnessapp.objects.all()

class IndexView(generic.ListView):
    template_name = 'dafitnessapp/index.html'
    model = dafitnessapp
    fields = ['message']
    success_url = reverse_lazy('dafitnessapp:home')


class ResultsView(generic.edit.CreateView):
    template_name = 'dafitnessapp/results.html'
    model = dafitnessapp
    fields = ['message']
    success_url = reverse_lazy('dafitnessapp:home')

class CreateView(generic.edit.CreateView):
    template_name = 'dafitnessapp/create.html'
    model = dafitnessapp
    fields = ['message']
    success_url = reverse_lazy('dafitnessapp:blogs') # more robust than hardcoding to /greetings/; directs user to index view after creating a greeting

class UpdateView(generic.edit.UpdateView):
    template_name = 'dafitnessapp/update.html'
    model = dafitnessapp
    fields = ['message']
    success_url = reverse_lazy('dafitnessapp:blogs')

class DeleteView(generic.edit.DeleteView):
    template_name = 'dafitnessapp/delete.html' # override default of greetings/greeting_confirm_delete.html
    model = dafitnessapp
    success_url = reverse_lazy('dafitnessapp:blogs')
    