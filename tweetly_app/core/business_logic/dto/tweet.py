from dataclasses import dataclass


@dataclass
class TweetDTO:
    author: str
    content: str
    count_likes: int
    count_retweets: int
    count_comments: int
