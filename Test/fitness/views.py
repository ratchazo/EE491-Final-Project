from django.views import generic
from django.urls import reverse_lazy
from .models import fitness

class IndexView(generic.ListView):
    template_name = 'fitness/index.html'
    context_object_name = 'fitness_list'

    def get_queryset(self):
        """Return the all greetings."""
        return fitness.objects.all()
