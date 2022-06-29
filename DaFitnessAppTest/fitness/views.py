from django.views import generic
from django.urls import reverse_lazy
from .models import fitness


class HomeView(generic.ListView):
    template_name = 'fitness/home.html'
    context_object_name = 'fitness_list'

    def get_queryset(self):
        """Return the all greetings."""
        return fitness.objects.all()

class IndexView(generic.ListView):
    template_name = 'fitness/index.html'
    model = fitness
    fields = ['message']
    success_url = reverse_lazy('fitness:home')


class ResultsView(generic.edit.CreateView):
    template_name = 'fitness/results.html'
    model = fitness
    fields = ['message']
    success_url = reverse_lazy('fitness:home')
    