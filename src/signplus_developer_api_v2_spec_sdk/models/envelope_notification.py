from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class EnvelopeNotification(BaseModel):
    """EnvelopeNotification

    :param subject: Subject of the notification, defaults to None
    :type subject: str, optional
    :param message: Message of the notification, defaults to None
    :type message: str, optional
    :param reminder_interval: Interval in days to send reminder, defaults to None
    :type reminder_interval: int, optional
    """

    subject: Optional[str] = Field(
        default=None, description="Subject of the notification"
    )
    message: Optional[str] = Field(
        default=None, description="Message of the notification"
    )
    reminder_interval: Optional[int] = Field(
        default=None, description="Interval in days to send reminder"
    )
