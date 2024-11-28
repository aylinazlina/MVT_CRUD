from django.forms import ModelForm
from .models import *
from django import forms


class CreatePlantForm(ModelForm):
    class Meta:
        model =Plants
        fields = '__all__'