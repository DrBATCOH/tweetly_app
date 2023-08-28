from .registration import singup, singup_confirmation, confirmation_email_stub
from .login import login_view
from .logout import logout_view
from .index import index
from .notification import notifications
from .profile import profile, edit_profile
from .trending import trending
from .tweet import add_tweet, get_tweet


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
    'trending',
    'edit_profile',
    'profile',
    'add_tweet'
]
