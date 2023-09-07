from django import forms


class TweetForm(forms.Form):
    content = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter text"}
        ),
        max_length=150,
    )
    tags = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={"placeholder": "Tags"}),
        max_length=150,
        required=False,
    )


class SearchTweetForm(forms.Form):
    tags = forms.CharField(
        label=False,
        max_length=30,
        widget=forms.TextInput(attrs={"placeholder": "Tags"}),
        strip=True,
        required=False,
    )
    author = forms.CharField(
        label=False,
        max_length=30,
        widget=forms.TextInput(attrs={"placeholder": "Author"}),
        strip=True,
        required=False,
    )
