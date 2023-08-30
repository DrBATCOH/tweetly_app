class ConfirmationCodeNotExists(Exception):
    ...


class ConfirmationCodeExpired(Exception):
    ...


class InvalidAuthCredentials(Exception):
    ...


class InvlidRegistrationAge(Exception):
    ...


class TweetNotFound(Exception):
    ...