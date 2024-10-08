from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .webhook import Webhook


@JsonMap({})
class ListWebhooksResponse(BaseModel):
    """ListWebhooksResponse

    :param webhooks: webhooks, defaults to None
    :type webhooks: List[Webhook], optional
    """

    def __init__(self, webhooks: List[Webhook] = None):
        """ListWebhooksResponse

        :param webhooks: webhooks, defaults to None
        :type webhooks: List[Webhook], optional
        """
        if webhooks is not None:
            self.webhooks = self._define_list(webhooks, Webhook)
