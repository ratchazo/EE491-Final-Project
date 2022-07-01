from django import forms

from .models import dafitnessapp


class CreateForm(forms.ModelForm):
    class Meta:
        model = dafitnessapp
        fields = ['title', 'text']
