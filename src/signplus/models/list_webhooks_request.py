from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .webhook_event import WebhookEvent


class ListWebhooksRequest(BaseModel):
    """ListWebhooksRequest

    :param webhook_id: ID of the webhook, defaults to None
    :type webhook_id: str, optional
    :param event: Event of the webhook, defaults to None
    :type event: WebhookEvent, optional
    """

    webhook_id: Optional[str] = Field(default=None, description="ID of the webhook")
    event: Optional[WebhookEvent] = Field(
        default=None, description="Event of the webhook"
    )
