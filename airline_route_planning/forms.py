from django import forms
from .models import Airport, Route

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['code', 'name', 'latitude', 'longitude']

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['origin', 'destination', 'distance']
