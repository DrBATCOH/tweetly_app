from datetime import date

from django.core.exceptions import ValidationError


class AgeValidator:
    def __init__(self, min_age: int) -> None:
        self.min_age = min_age

    def __call__(self, value: date) -> None:
        today = date.today()
        age = (
            today.year
            - value.year
            - ((today.month, today.day) < (value.month, value.day))
        )
        if age < self.min_age:
            raise ValidationError(
                f"You must be at least {self.min_age} years old to register."
            )
        else:
            return None
