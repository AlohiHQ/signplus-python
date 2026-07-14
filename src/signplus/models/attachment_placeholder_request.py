from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AttachmentPlaceholderRequest(BaseModel):
    """AttachmentPlaceholderRequest

    :param recipient_id: ID of the recipient
    :type recipient_id: str
    :param id_: ID of the attachment placeholder, defaults to None
    :type id_: str, optional
    :param name: name
    :type name: str
    :param hint: Hint of the attachment placeholder, defaults to None
    :type hint: str, optional
    :param required: Whether the attachment placeholder is required
    :type required: bool
    :param multiple: multiple
    :type multiple: bool
    """

    recipient_id: str = Field(description="ID of the recipient")
    id_: Optional[str] = Field(
        alias="id",
        serialization_alias="id",
        default=None,
        description="ID of the attachment placeholder",
    )
    name: str
    hint: Optional[str] = Field(
        default=None, description="Hint of the attachment placeholder"
    )
    required: bool = Field(description="Whether the attachment placeholder is required")
    multiple: bool
