from django import forms
from .models import *


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = "__all__"


class PartsForm(forms.Form):
    name = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
    process = forms.ModelChoiceField(queryset=Process.objects.all())

    class Meta:
        model = Part
        fields = "__all__"
