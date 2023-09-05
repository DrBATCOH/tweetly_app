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


def replace_swear_word_in_text(value: str) -> str:
    censored_text = value
    for word in swear_words:
        if word in value.lower():
            censored_text = censored_text.replace(word[1:-1], "*" * (len(word) - 2))
    return censored_text
