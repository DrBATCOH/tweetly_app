from django.core.exceptions import ValidationError
from django.core.files import File


class ValidateFileSize:
    def __init__(self, max_size: int) -> None:
        self._max_size = max_size

    def __call__(self, value: File) -> None:
        if value.size > self._max_size:
            max_size = int(self._max_size / 1_000_000)
            raise ValidationError(message=f"Max file size {max_size} MB")
