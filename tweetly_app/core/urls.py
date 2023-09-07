from core.presentation.views import (
    add_tweet,
    all_follower,
    all_following,
    author_profile,
    confirmation_email_stub,
    follow,
    get_populate_tag_by_country,
    get_tweet_whit_comment,
    index,
    like_tweet,
    login_view,
    logout_view,
    make_retweet,
    show_notifications,
    singup,
    singup_confirmation,
    tweet_by_tag,
    unfollow,
    user_profile,
    edit_profile
)


from django.urls import path

urlpatterns = [
    path("", index, name="home"),
    path("trending/", get_populate_tag_by_country, name="trending"),
    path("profile/", user_profile, name="profile"),
    path("author/<str:username>/", author_profile, name="author_profile"),
    path("notifications/", show_notifications, name="notifications"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("singup/", singup, name="singup"),
    path("confirmation/", singup_confirmation, name="confirm-singup"),
    path("confir/note/", confirmation_email_stub, name="confirm-stub"),
    path("tweet_list/<int:tweet_id>", get_tweet_whit_comment, name="tweet"),
    path("add_tweet", add_tweet, name="add_tweet"),
    path("tweet_by_tag/<str:tag_name>/", tweet_by_tag, name="tweet_by_tag"),
    path("like/<int:tweet_id>/", like_tweet, name="like_tweet"),
    path("retweet/<int:tweet_id>/", make_retweet, name="retweet"),
    path("follow/<str:username>/", follow, name="follow"),
    path("unfollow/<str:username>/", unfollow, name="unfollow"),
    path("followers/", all_follower, name="follower"),
    path("following/", all_following, name="following"),
    path("edit/", edit_profile, name="edit_profile"),
]
