# from __future__ import annotations

# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from core.models import CustomUser

# from core.models import Tweet, CustomUser
# from core.business_logic.exceptions import SelfLikeError




# def get_profile_info(username: str):
#     """Gets info about user and his tweets from DB."""

#     user = CustomUser(username=username)
#     user_tweets = get_user_tweets(user=user)
#     profile = ProfileDTO(
#         user=user,
#         user_tweets=user_tweets,
#     )
#     return profile