from django import forms
from . import models

class BrandForm(forms.ModelForm):
    model = models.Brand
    fields = ['name', 'description']
