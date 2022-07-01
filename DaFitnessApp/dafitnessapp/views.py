from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic
from django.urls import reverse_lazy
from .models import dafitnessapp
from django.contrib.auth.models import User
from .forms import CreateForm

class HomeView(generic.ListView):
    template_name = 'dafitnessapp/home.html'
    context_object_name = 'dafitnessapp_list'

    def get_queryset(self):
        return dafitnessapp.objects.all()

class IndexView(generic.ListView):
    template_name = 'dafitnessapp/index.html'
    context_object_name = 'dafitnessapp_list'

    def get_queryset(self):
        return dafitnessapp.objects.all()

class ResultsView(generic.ListView):
    template_name = 'dafitnessapp/results.html'
    context_object_name = 'dafitnessapp_list'

    def get_queryset(self):
        return dafitnessapp.objects.all()

class CommentsView(generic.ListView):
    template_name = 'dafitnessapp/comments.html'
    context_object_name = 'dafitnessapp_list'

    def get_queryset(self):
        return dafitnessapp.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'dafitnessapp/create.html'
    model = dafitnessapp
    fields = ['author','title', 'text']
    success_url = reverse_lazy('dafitnessapp:home')

def create_view(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('dafitnessapp:comments')
    else:
        form = CreateForm()
    return render(request,'dafitnessapp/create.html', {'form': form})

class UpdateView(generic.edit.UpdateView):
    template_name = 'dafitnessapp/update.html'
    model = dafitnessapp
    fields = ['title', 'text']
    success_url = reverse_lazy('dafitnessapp:comments')

class DeleteView(generic.edit.DeleteView):
    template_name = 'dafitnessapp/delete.html'
    model = dafitnessapp
    success_url = reverse_lazy('dafitnessapp:home')