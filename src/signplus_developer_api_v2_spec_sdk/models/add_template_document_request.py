from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class AddTemplateDocumentRequest(BaseModel):
    """AddTemplateDocumentRequest

    :param file: File to upload in binary format
    :type file: bytes
    """

    file: bytes = Field(description="File to upload in binary format")
