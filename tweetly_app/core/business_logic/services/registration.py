from __future__ import annotations

import logging
import time
import uuid
from typing import TYPE_CHECKING

from core.business_logic.exceptions import (
    ConfirmationCodeExpired,
    ConfirmationCodeNotExists,
)
from core.models import CustomUser
from django.core.mail import send_mail
from django.urls import reverse

if TYPE_CHECKING:
    from core.business_logic.dto import RegistrationDTO

from core.models import EmailConfirmationCodes
from django.conf import settings

logger = logging.getLogger(__name__)


def create_user(data: RegistrationDTO) -> None:
    logger.info("Get user creation request.", extra={"userdata": str(data)})

    user = CustomUser

    create_user = user.objects.create_user(
        first_name=data.first_name,
        last_name=data.last_name,
        username=data.username,
        email=data.email,
        password=data.password,
        country=data.country,
        birthdate=data.birthdate,
        is_active=False,
    )

    confirmation_code = str(uuid.uuid4())
    exp_time = int(time.time()) + settings.CONFIRMATION_CODE_LIFETIME
    EmailConfirmationCodes.objects.create(
        code=confirmation_code, user=create_user, expiration=exp_time
    )

    confirmation_url = (
        settings.SERVER_HOST + reverse("confirm-singup") + f"?code={confirmation_code}"
    )
    send_mail(
        subject="Confirn your email",
        message=f"Please confirm email by clicking the link below:\n\n{confirmation_url}",
        from_email=settings.EMAIL_FROM,
        recipient_list=[data.email],
    )


def confirm_user_registration(confirmation_code: str) -> None:
    try:
        code_data = EmailConfirmationCodes.objects.get(code=confirmation_code)
    except EmailConfirmationCodes.DoesNotExist as err:
        logger.error(
            "Provided code doesn't exists.",
            exc_info=err,
            extra={"code": confirmation_code},
        )
        raise ConfirmationCodeNotExists

    if time.time() > code_data.expiration:
        logger.info(
            "Provided expiration code expired.",
            extra={
                "current_time": str(time.time()),
                "code_expiration": str(code_data.expiration),
            },
        )
        raise ConfirmationCodeExpired

    user = code_data.user
    user.is_active = True
    user.save()

    code_data.delete()
