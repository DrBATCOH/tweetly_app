from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.models import CustomUser

from core.models import Notification, UserNotification


def create_notification(recipient: CustomUser, message: str) -> None:
    notification = Notification.objects.create(
        message=message,
    )
    UserNotification.objects.create(
        user=recipient,
        notification=notification,
    )


def get_notification(user: CustomUser) -> Notification:
    notifications = UserNotification.objects.filter(user=user)

    return notifications
