from django.shortcuts import render
from core.presentation.forms import TweetForm
from core.models.tweet import TweetModel


def index(request):
    tweets = TweetModel.objects.all()
    form = TweetForm(request.POST)
    return render(request, "index.html", {"form": form, "tweets": tweets})
