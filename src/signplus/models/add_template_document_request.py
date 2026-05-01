from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class AddTemplateDocumentRequest(BaseModel):
    """AddTemplateDocumentRequest

    :param file: file, defaults to None
    :type file: bytes, optional
    """

    file: Optional[bytes] = Field(default=None)
