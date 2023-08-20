from django.shortcuts import render


def tags(request):
    return render(request=request, template_name="tags.html")
