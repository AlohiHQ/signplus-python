from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class AddEnvelopeDocumentRequest(BaseModel):
    """AddEnvelopeDocumentRequest

    :param file: File to upload in binary format, defaults to None
    :type file: bytes, optional
    """

    file: Optional[bytes] = Field(
        default=None, description="File to upload in binary format"
    )
