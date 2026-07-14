from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .webhook_event import WebhookEvent


class Webhook(BaseModel):
    """Webhook

    :param id_: Unique identifier of the webhook, defaults to None
    :type id_: str, optional
    :param event: Event of the webhook, defaults to None
    :type event: WebhookEvent, optional
    :param target: Target URL of the webhook, defaults to None
    :type target: str, optional
    """

    id_: Optional[str] = Field(
        alias="id",
        serialization_alias="id",
        default=None,
        description="Unique identifier of the webhook",
    )
    event: Optional[WebhookEvent] = Field(
        default=None, description="Event of the webhook"
    )
    target: Optional[str] = Field(default=None, description="Target URL of the webhook")
