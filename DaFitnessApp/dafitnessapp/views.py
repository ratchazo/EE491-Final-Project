from django.views import generic
from django.urls import reverse_lazy
from .models import dafitnessapp


class HomeView(generic.ListView):
    template_name = 'dafitnessapp/home.html'
    context_object_name = 'dafitnessapp'

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
