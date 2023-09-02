from .registration import singup, singup_confirmation, confirmation_email_stub
from .login import login_view
from .logout import logout_view
from .index import index
from .notification import notifications
from .profile import profile, edit_profile
from .trending import get_populate_tag_by_country
from .tweet import add_tweet, get_tweet, tweet_by_tag
from .like import like_tweet
from .retweet import make_retweet
from .comment import add_comment


__all__ = [
    'singup',
    'singup_confirmation',
    'confirmation_email_stub',
    'login_view',
    'logout_view',
    'index',
    'get_tweet',
    'notifications',
    'profile',
    'get_populate_tag_by_country',
    'edit_profile',
    'profile',
    'add_tweet',
    'tweet_by_tag',
    'like_tweet',
    'make_retweet',
    'add_comment'
]
