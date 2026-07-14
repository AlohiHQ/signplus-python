from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AddTemplateDocumentRequest(BaseModel):
    """AddTemplateDocumentRequest

    :param file: File to upload in binary format
    :type file: bytes
    """

    file: bytes = Field(description="File to upload in binary format")
