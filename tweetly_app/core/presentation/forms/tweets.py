from django import forms
from core.models import TweetModel


class TweetForm(forms.ModelForm):
    class Meta:
        model = TweetModel
        fields = ['author', 'content']
