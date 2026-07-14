from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .webhook_event import WebhookEvent


class CreateWebhookRequest(BaseModel):
    """CreateWebhookRequest

    :param event: Event of the webhook
    :type event: WebhookEvent
    :param target: URL of the webhook target
    :type target: str
    """

    event: WebhookEvent = Field(description="Event of the webhook")
    target: str = Field(description="URL of the webhook target")
