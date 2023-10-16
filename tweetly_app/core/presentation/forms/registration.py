from core.models import CountryModel
from core.validators import AgeValidator
from django import forms
from django.db.utils import ProgrammingError


class TableNotExists(Exception):
    ...


def get_all_contries() -> list:
    try:
        country = [(country.name, country.name) for country in CountryModel.objects.all()]
    except ProgrammingError:
        return []
    return country


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label=False,
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "First name"}),
    )
    last_name = forms.CharField(
        label=False,
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Last name"}),
    )
    username = forms.CharField(
        label=False,
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Nickname"}),
    )
    email = forms.EmailField(
        label=False,
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
    )
    password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
        max_length=100,
        required=True,
    )
    country = forms.ChoiceField(
        label=False, choices=get_all_contries(), initial="Country", required=True
    )
    birthdate = forms.DateField(
        label=False,
        required=True,
        validators=[AgeValidator(min_age=18)],
        widget=forms.SelectDateWidget(years=range(1940, 2023)),
    )
