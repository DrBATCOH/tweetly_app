from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.http import HttpRequest

from core.business_logic.dto import SearchTweetDTO
from core.business_logic.services import calculate_comment_counts, search_tweet
from core.presentation.converters import convert_data_from_form_to_dto
from core.presentation.forms import SearchTweetForm
from core.presentation.paginator import CustomPagination, PageNotExists
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(request_method_list=["GET"])
def index(request: HttpRequest) -> HttpResponse:
    form = SearchTweetForm(request.GET)

    if form.is_valid():
        search_filters = convert_data_from_form_to_dto(
            SearchTweetDTO, form.cleaned_data
        )
        tweets = search_tweet(search_filters)

        calculate_comment_counts(tweets)

        page_number = request.GET.get("page", 1)
        paginator = CustomPagination(per_page=5)

        try:
            tweets_paginated = paginator.paginate(data=tweets, page_number=page_number)
        except PageNotExists:
            return HttpResponseBadRequest("Page doesn't exist.")

        form = SearchTweetForm()
        context = {
            "tweets": tweets_paginated.data,
            "form": form,
            "next_page": tweets_paginated.next_page,
            "prev_page": tweets_paginated.prev_page,
        }

        return render(request=request, template_name="index.html", context=context)
    else:
        context = {"form": form}
        return render(request=request, template_name="index.html", context=context)
