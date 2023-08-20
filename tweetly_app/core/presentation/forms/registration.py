from django import forms
from core.models import CountryModel

COUNTRY = [(country.name, country.name) for country in CountryModel.objects.all()]


class RegistrationForm(forms.Form):
    username = forms.CharField(label=False, max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label=False, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), max_length=100, required=True)
    country = forms.ChoiceField(label=False, choices=COUNTRY, initial="Country", required=True)
    birthdate = forms.DateField(label=False, required=True, widget=forms.SelectDateWidget(years=range(1960, 2023)))
