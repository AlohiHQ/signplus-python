from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class SetEnvelopeNotificationRequest(BaseModel):
    """SetEnvelopeNotificationRequest

    :param subject: subject, defaults to None
    :type subject: str, optional
    :param message: message, defaults to None
    :type message: str, optional
    :param reminder_interval: reminder_interval, defaults to None
    :type reminder_interval: float, optional
    """

    subject: Optional[str] = Field(default=None)
    message: Optional[str] = Field(default=None)
    reminder_interval: Optional[float] = Field(default=None)
