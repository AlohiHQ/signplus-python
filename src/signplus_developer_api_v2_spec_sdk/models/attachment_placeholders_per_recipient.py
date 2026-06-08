from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel
from .attachment_placeholder import AttachmentPlaceholder


class AttachmentPlaceholdersPerRecipient(BaseModel):
    """AttachmentPlaceholdersPerRecipient

    :param recipient_id: ID of the recipient, defaults to None
    :type recipient_id: str, optional
    :param recipient_name: Name of the recipient, defaults to None
    :type recipient_name: str, optional
    :param placeholders: placeholders, defaults to None
    :type placeholders: List[AttachmentPlaceholder], optional
    """

    recipient_id: Optional[str] = Field(default=None, description="ID of the recipient")
    recipient_name: Optional[str] = Field(
        default=None, description="Name of the recipient"
    )
    placeholders: Optional[List[AttachmentPlaceholder]] = Field(default=None)
