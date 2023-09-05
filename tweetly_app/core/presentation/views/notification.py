from __future__ import annotations

from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.shortcuts import render

if TYPE_CHECKING:
    from django.http import HttpRequest

from core.business_logic.services import get_notification


def show_notifications(request: HttpRequest) -> HttpResponse:
    user = request.user
    notifications = get_notification(user=user)
    context = {"notifications": notifications}
    return render(request, "notifications.html", context)
