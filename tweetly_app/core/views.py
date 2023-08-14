from django.shortcuts import render


def index(request):
    return render (request=request, template_name="index.html")


def trending(request):
    return render (request=request, template_name="trending.html")


def profile(request):
    return render (request=request, template_name="profile.html")


def tags(request):
    return render (request=request, template_name="tags.html")


def notifications(request):
    return render (request=request, template_name="notifications.html")
