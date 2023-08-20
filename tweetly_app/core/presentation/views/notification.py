from django.shortcuts import render, redirect


def notifications(request):
    return render(request=request, template_name="notifications.html")
