from django.urls import path
from core.presentation.views import (
    index,
    profile,
    notifications,
    get_populate_tag_by_country,
    login_view,
    logout_view,
    singup,
    singup_confirmation,
    confirmation_email_stub,
    get_tweet,
    add_tweet,
    tweet_by_tag,
    like_tweet,
    make_retweet,
    add_comment
)


urlpatterns = [
    path("", index, name="home"),
    path("trending/", get_populate_tag_by_country, name="trending"),
    path('profile/', profile, name='profile'),
    path("notifications/", notifications, name="notifications"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("singup/", singup, name="singup"),
    path("confirmation/", singup_confirmation, name="confirm-singup"),
    path("confir/note/", confirmation_email_stub, name="confirm-stub"),
    path("tweet_list/<int:tweet_id>", get_tweet, name="tweet"),
    path("add_tweet", add_tweet, name="add_tweet"),
    path('tweet_by_tag/<str:tag_name>/', tweet_by_tag, name='tweet_by_tag'),
    path("like/<int:tweet_id>/", like_tweet, name="like_tweet"),
    path("retweet/<int:tweet_id>/", make_retweet, name="retweet"),
    path("comment/<int:tweet_id>/", add_comment, name="comment"),
]
