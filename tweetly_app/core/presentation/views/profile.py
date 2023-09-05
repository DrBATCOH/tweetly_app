from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

if TYPE_CHECKING:
    from django.http import HttpRequest

from core.business_logic.services import get_author_profile, get_user_profile


@require_http_methods(request_method_list=["GET", "POST"])
@login_required
def user_profile(request: HttpRequest) -> HttpResponse:
    user = request.user
    user_data = get_user_profile(
        user_profile=user, page_number=request.GET.get("page", 1)
    )

    context = {"user": user, "data": user_data}

    return render(request=request, template_name="user_profile.html", context=context)


@require_http_methods(request_method_list=["GET", "POST"])
@login_required
def author_profile(request: HttpRequest, username: str) -> HttpResponse:
    author_data = get_author_profile(request=request, username=username)
    context = {"data": author_data}

    return render(request=request, template_name="author_profile.html", context=context)


def edit_profile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, "edit_profile.html", {"form": form})
