from dataclasses import dataclass
from core.models import Tag, Tweet
from django.db.models import QuerySet


@dataclass
class TagDTO:
    name: str


@dataclass
class TweetTagDTO:
    tweets: QuerySet[Tweet]
    tag: Tag
