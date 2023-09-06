from django.core.exceptions import ValidationError
from django.core.files import File


class ValidateFileExtension:
    def __init__(self, available_extensions: list[str]) -> None:
        self._available_extensions = available_extensions

    def __call__(self, value: File) -> None:
        split_file_name = value.name.split(".")
        if len(split_file_name) < 2:
            raise ValidationError(message=f"Accept only {self._available_extensions}")

        file_extension = split_file_name[-1]

        if file_extension not in self._available_extensions:
            raise ValidationError(message=f"Accept only {self._available_extensions}")
