from __future__ import annotations

import logging

from typing import TYPE_CHECKING
from core.models import CustomUser


if TYPE_CHECKING:
    from core.business_logic.dto import RegistrationDTO


logger = logging.getLogger(__name__)


def create_user(data: RegistrationDTO) -> None:
    logger.info("Get user creation request.", extra={"userdata": str(data)})

    CustomUser.objects.create_user(
        username=data.username,
        email=data.email,
        password=data.password,
        country=data.country,
        birthdate=data.birthdate,
        is_active=False
    )
