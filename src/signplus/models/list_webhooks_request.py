from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class ListWebhooksRequest(BaseModel):
    """ListWebhooksRequest

    :param webhook_id: webhook_id, defaults to None
    :type webhook_id: str, optional
    :param event: event, defaults to None
    :type event: str, optional
    """

    webhook_id: Optional[str] = Field(default=None)
    event: Optional[str] = Field(default=None)
