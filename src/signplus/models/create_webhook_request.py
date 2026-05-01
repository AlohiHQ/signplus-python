from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class CreateWebhookRequest(BaseModel):
    """CreateWebhookRequest

    :param event: event, defaults to None
    :type event: str, optional
    :param target: target, defaults to None
    :type target: str, optional
    """

    event: Optional[str] = Field(default=None)
    target: Optional[str] = Field(default=None)
