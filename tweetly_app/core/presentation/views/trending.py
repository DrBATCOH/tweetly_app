from __future__ import annotations
from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


if TYPE_CHECKING:
    from django.http import HttpRequest


from core.business_logic.services import get_tags_by_country


@require_http_methods(request_method_list=["GET"])
def get_populate_tag_by_country(request: HttpRequest) -> HttpResponse:
    user = request.user
    country = user.country
    tags = get_tags_by_country(country=country)
    print(tags)
    context = {"tags": tags}
    return render(request=request, template_name="trending.html", context=context)
