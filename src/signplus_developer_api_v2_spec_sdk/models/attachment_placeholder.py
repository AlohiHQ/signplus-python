from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel
from .attachment_placeholder_file import AttachmentPlaceholderFile


class AttachmentPlaceholder(BaseModel):
    """AttachmentPlaceholder

    :param recipient_id: ID of the recipient, defaults to None
    :type recipient_id: str, optional
    :param id_: ID of the attachment placeholder, defaults to None
    :type id_: str, optional
    :param name: Name of the attachment placeholder, defaults to None
    :type name: str, optional
    :param hint: Hint of the attachment placeholder, defaults to None
    :type hint: str, optional
    :param required: Whether the attachment placeholder is required, defaults to None
    :type required: bool, optional
    :param multiple: Whether the attachment placeholder can have multiple files, defaults to None
    :type multiple: bool, optional
    :param files: files, defaults to None
    :type files: List[AttachmentPlaceholderFile], optional
    """

    recipient_id: Optional[str] = Field(default=None, description="ID of the recipient")
    id_: Optional[str] = Field(
        alias="id",
        serialization_alias="id",
        default=None,
        description="ID of the attachment placeholder",
    )
    name: Optional[str] = Field(
        default=None, description="Name of the attachment placeholder"
    )
    hint: Optional[str] = Field(
        default=None, description="Hint of the attachment placeholder"
    )
    required: Optional[bool] = Field(
        default=None, description="Whether the attachment placeholder is required"
    )
    multiple: Optional[bool] = Field(
        default=None,
        description="Whether the attachment placeholder can have multiple files",
    )
    files: Optional[List[AttachmentPlaceholderFile]] = Field(default=None)
