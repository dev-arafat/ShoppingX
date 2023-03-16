from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Customer


class CoustomerProfile(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'state', 'zipCode']
        widgets = {
                      'name': forms.TextInput(attrs={'class':'form-control'}),
                      'locality': forms.TextInput(attrs={'class':'form-control'}),
                      'city': forms.TextInput(attrs={'class':'form-control'}),
                      'state': forms.Select(attrs={'class':'form-control'}),
                      'zipCode': forms.NumberInput(attrs={'class':'form-control'}),
                }
