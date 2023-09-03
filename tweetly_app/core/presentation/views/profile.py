from __future__ import annotations
from typing import TYPE_CHECKING

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model 
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.db.models import Q
from django.utils import timezone


if TYPE_CHECKING:
    from django.http import HttpRequest


from core.models import Follower, Tweet
from core.presentation.paginator import CustomPagination, PageNotExists


@require_http_methods(request_method_list=["GET", "POST"])
@login_required
def user_profile(request: HttpRequest) -> HttpResponse:
    user_profile = request.user
    last_login = user_profile.last_login
    is_online = (timezone.now() - last_login).seconds > 300
    tweets = Tweet.objects.filter(Q(author=user_profile) | Q(retweet__user=user_profile)).order_by("-created_at")
    page_number = request.GET.get("page", 1)
    paginator = CustomPagination(per_page=4)

    try:
        tweets_paginated = paginator.paginate(data=tweets, page_number=page_number)
    except PageNotExists:
        return HttpResponseBadRequest("Page doesn't exist.")

    context = {
        "is_online": is_online,
        "paginated": tweets_paginated.data,
        "next_page": tweets_paginated.next_page,
        "prev_page": tweets_paginated.prev_page,
        "profile": user_profile,
        "is_user_profile": True,
        
    }

    return render(request=request, template_name="profile.html", context=context)



@require_http_methods(request_method_list=["GET", "POST"])
def author_profile(request: HttpRequest, username: str) -> HttpResponse:
    author_profile = get_object_or_404(get_user_model(), username=username)
    last_login = author_profile.last_login
    is_online = (timezone.now() - last_login).seconds > 300
    tweets = Tweet.objects.filter(Q(author=author_profile) | Q(retweet__user=author_profile)).order_by("-created_at")
    page_number = request.GET.get("page", 1)
    paginator = CustomPagination(per_page=4)
    is_following = False

    if request.user.is_authenticated:
        is_following = Follower.objects.filter(
            follower=author_profile, following=request.user
    ).exists()

    try:
        tweets_paginated = paginator.paginate(data=tweets, page_number=page_number)
    except PageNotExists:
        return HttpResponseBadRequest("Page doesn't exist.")

    context = {
        "is_online": is_online,
        "paginated": tweets_paginated.data,
        "next_page": tweets_paginated.next_page,
        "prev_page": tweets_paginated.prev_page,
        "profile": author_profile,
        "is_following": is_following,
        "is_user_profile": False
    }

    return render(request=request, template_name="profile.html", context=context)





def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})
