from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}), required=False)
    password = forms.CharField(label=False, max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=False)
