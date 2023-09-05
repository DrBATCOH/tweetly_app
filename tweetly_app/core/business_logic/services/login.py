from __future__ import annotations

from typing import TYPE_CHECKING

from core.business_logic.exceptions import InvalidAuthCredentials
from django.contrib.auth import authenticate

if TYPE_CHECKING:
    from core.business_logic.dto import LoginDTO
    from django.contrib.auth.models import AbstractUser


def authenticate_user(data: LoginDTO) -> AbstractUser:
    user = authenticate(email=data.email, password=data.password)

    if user:
        return user
    else:
        raise InvalidAuthCredentials
