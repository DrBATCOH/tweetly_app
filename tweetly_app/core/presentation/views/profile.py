from __future__ import annotations
from typing import TYPE_CHECKING

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.utils import timezone


if TYPE_CHECKING:
    from django.http import HttpRequest


from core.presentation.converters import convert_data_from_form_to_dto
from core.business_logic.services import create_tweet, get_tweet_by_id
from core.presentation.forms import TweetForm
from core.business_logic.dto import TweetDTO
from core.models import CustomUser, Tweet
from core.presentation.paginator import CustomPagination, PageNotExists


@require_http_methods(request_method_list=["GET", "POST"])
@login_required
def profile(request: HttpRequest) -> HttpResponse:

    user = request.user
    last_login = user.last_login
    is_online = (timezone.now() - last_login).seconds > 300
    user_tweet = Tweet.objects.filter(author=user).order_by("-created_at")
    page_number = request.GET.get("page", 1)
    paginator = CustomPagination(per_page=3)
    print(user_tweet)
    try:
        tweets_paginated = paginator.paginate(data=user_tweet, page_number=page_number)
    except PageNotExists:
        return HttpResponseBadRequest("Page doesn't exist.")

    context = {"is_online": is_online,
               "paginated": tweets_paginated.data,
               "next_page": tweets_paginated.next_page,
               "prev_page": tweets_paginated.prev_page
               }

    return render(request=request, template_name="profile.html", context=context)


user = CustomUser


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Перенаправляем на страницу профиля после успешного обновления
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})

