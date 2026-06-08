from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class RenameEnvelopeRequest(BaseModel):
    """RenameEnvelopeRequest

    :param name: Name of the envelope, defaults to None
    :type name: str, optional
    """

    name: Optional[str] = Field(default=None, description="Name of the envelope")
