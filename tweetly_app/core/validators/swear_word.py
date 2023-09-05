from django.core.exceptions import ValidationError

swear_words = [
    "fuck",
    "gay",
    "asshole",
    "jerk",
    "bastard",
    "bitch",
    "nigger",
    "faggot",
    "homo",
    "fucked",
    "fucking",
    "idiot",
    "dick",
    "pussy",
]


def validate_swear_word_in_nickname(value: str) -> None:
    for word in swear_words:
        if word in value.lower():
            raise ValidationError(message="swear word")
        return None
