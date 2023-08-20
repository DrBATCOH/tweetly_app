from django.shortcuts import render, redirect


def trending(request):
    return render(request=request, template_name="trending.html")
