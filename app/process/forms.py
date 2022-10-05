from django import forms
from .models import *


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = "__all__"


class PartsForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = "__all__"
