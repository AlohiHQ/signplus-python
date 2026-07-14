from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .webhook import Webhook


class ListWebhooksResponse(BaseModel):
    """ListWebhooksResponse

    :param webhooks: webhooks, defaults to None
    :type webhooks: List[Webhook], optional
    """

    webhooks: Optional[List[Webhook]] = Field(default=None)
