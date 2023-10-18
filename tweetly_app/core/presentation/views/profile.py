from __future__ import annotations

from typing import TYPE_CHECKING


from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods


if TYPE_CHECKING:
    from django.http import HttpRequest

from core.business_logic.services import get_author_profile, get_user_profile, edit_user_profile
from core.presentation.forms import EditProfileForm
from core.presentation.converters import convert_data_from_form_to_dto
from core.business_logic.dto import ProfileDTO


@require_http_methods(request_method_list=["GET"])
def user_profile(request: HttpRequest) -> HttpResponse:
    user = request.user
    user_data = get_user_profile(
        user_profile=user, page_number=request.GET.get("page", 1)
    )

    context = {"user": user, "data": user_data}

    return render(request=request, template_name="user_profile.html", context=context)


@require_http_methods(request_method_list=["GET"])
def author_profile(request: HttpRequest, username: str) -> HttpResponse:
    author_data = get_author_profile(request=request, username=username)
    context = {"data": author_data}

    return render(request=request, template_name="author_profile.html", context=context)


@require_http_methods(request_method_list=["GET", "POST"])
def edit_profile(request: HttpRequest) -> HttpResponse:
    user = request.user
    user_data = {
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "username": request.user.username,
        "email": request.user.email,
        "birthdate": request.user.birthdate,
        "status": request.user.status,
        "old_email": request.user.email,
        "country": request.user.country
    }

    if request.method == "GET":
        form = EditProfileForm(user_data)
        context = {"form": form}
        return render(request=request, template_name="edit_profile.html", context=context)
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = convert_data_from_form_to_dto(ProfileDTO, form.cleaned_data)
            edit_user_profile(data=data, user=user)
            return redirect(to="profile")
        else:
            context = {"form": form}
            return render(request, "edit_profile.html", context)
