from __future__ import annotations

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from django.http import HttpRequest

from core.presentation.forms import RegistrationForm
from core.business_logic.dto import RegistrationDTO
from core.presentation.converters import convert_data_from_form_to_dto
from core.business_logic.services import create_user, confirm_user_registration
from core.business_logic.exceptions import ConfirmationCodeNotExists, ConfirmationCodeExpired


@require_http_methods(["GET", "POST"])
def singup(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = RegistrationForm()
        context = {"form": form}
        return render(request=request, template_name="singup.html", context=context)

    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = convert_data_from_form_to_dto(dto=RegistrationDTO, data_from_form=form.cleaned_data)
            create_user(data=data)
            return redirect(to="confirm-stub")
        else:
            context = {"form": form, "error_message": "Registration only from 18 years old."}
            return render(request, 'singup.html', context)


@require_http_methods(["GET"])
def confirmation_email_stub(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Confirmation email sent. Please confirm it by the link.")


@require_http_methods(["GET"])
def singup_confirmation(request: HttpRequest) -> HttpResponse:
    confirmation_code = request.GET["code"]
    try:
        confirm_user_registration(confirmation_code=confirmation_code)
    except ConfirmationCodeNotExists:
        return HttpResponseBadRequest(content="Invalid confirmation code")
    except ConfirmationCodeExpired:
        return HttpResponseBadRequest(content="Confirmation code expired")

    return redirect(to="home")
