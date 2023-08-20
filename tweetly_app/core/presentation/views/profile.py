from django.shortcuts import render, redirect


def profile(request):
    return render(request=request, template_name="profile.html")
