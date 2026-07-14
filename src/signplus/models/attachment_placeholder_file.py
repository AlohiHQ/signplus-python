from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AttachmentPlaceholderFile(BaseModel):
    """AttachmentPlaceholderFile

    :param id_: ID of the file, defaults to None
    :type id_: str, optional
    :param name: Name of the file, defaults to None
    :type name: str, optional
    :param size: Size of the file in bytes, defaults to None
    :type size: int, optional
    :param mimetype: MIME type of the file, defaults to None
    :type mimetype: str, optional
    """

    id_: Optional[str] = Field(
        alias="id", serialization_alias="id", default=None, description="ID of the file"
    )
    name: Optional[str] = Field(default=None, description="Name of the file")
    size: Optional[int] = Field(default=None, description="Size of the file in bytes")
    mimetype: Optional[str] = Field(default=None, description="MIME type of the file")
