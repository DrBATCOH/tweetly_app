from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter text'}),
        max_length=150,
    )
