from django.urls import path
from core.presentation.views import (
    index,
    profile,
    notifications,
    trending,
    login_view,
    logout_view,
    singup,
    singup_confirmation,
    confirmation_email_stub,
    get_tweet,
    add_tweet,

)


urlpatterns = [
    path("", index, name="home"),
    path("trending/", trending, name="trending"),
    path('profile/', profile, name='profile'),
    path("notifications/", notifications, name="notifications"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("singup/", singup, name="singup"),
    path("confirmation/", singup_confirmation, name="confirm-singup"),
    path("confir/note/", confirmation_email_stub, name="confirm-stub"),
    path("tweet_list/<int:tweet_id>", get_tweet, name="tweet"),
    path("add_tweet", add_tweet, name="add_tweet"),
]
