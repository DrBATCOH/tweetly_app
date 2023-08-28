from dataclasses import dataclass


@dataclass
class TweetDTO:
    content: str
    tags: str


@dataclass
class SearchTweetDTO:
    tags: str
    author: str
