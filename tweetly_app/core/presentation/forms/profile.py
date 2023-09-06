from core.models import CountryModel
from core.validators import AgeValidator, ValidateFileExtension, ValidateFileSize
from django import forms

COUNTRY = [(country.name, country.name) for country in CountryModel.objects.all()]


class EditProfileForm(forms.Form):
    avatar = forms.ImageField(
        label=False,
        allow_empty_file=False,
        required=False,
        validators=[ValidateFileExtension(["png", "jpeg", "jpg"]), ValidateFileSize(max_size=5_000_000)],
        widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "avatar"}))
    status = forms.CharField(
        label=False,
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "status"}))
    first_name = forms.CharField(
        label=False,
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "First name"}),
    )
    last_name = forms.CharField(
        label=False,
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Last name"}),
    )
    username = forms.CharField(
        label=False,
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Nickname"}),
    )
    email = forms.EmailField(
        label=False,
        required=False,
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
    )
    old_password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Old password"}),
        max_length=100,
        required=False,
    )
    new_password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={"placeholder": "New password"}),
        max_length=100,
        required=False,
    )
    country = forms.ChoiceField(
        label=False, choices=COUNTRY, initial="Country", required=False
    )
    birthdate = forms.DateField(
        label=False,
        required=True,
        validators=[AgeValidator(min_age=18)],
        widget=forms.SelectDateWidget(years=range(1940, 2023)),
    )
