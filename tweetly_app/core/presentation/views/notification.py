from __future__ import annotations

from typing import TYPE_CHECKING

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

if TYPE_CHECKING:
    from django.http import HttpRequest

from core.business_logic.services import get_notification
from core.presentation.paginator import CustomPagination, PageNotExists


def show_notifications(request: HttpRequest) -> HttpResponse:
    user = request.user
    notification = get_notification(user=user)
    page_number = request.GET.get("page", 1)
    paginator = CustomPagination(per_page=14)
    try:
        notifications = paginator.paginate(data=notification, page_number=page_number)
    except PageNotExists:
        raise HttpResponseBadRequest("Page doesn't exist.")
    context = {"notifications": notifications}
    return render(request, "notifications.html", context)
