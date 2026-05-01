from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class SetEnvelopeCommentRequest(BaseModel):
    """SetEnvelopeCommentRequest

    :param comment: comment, defaults to None
    :type comment: str, optional
    """

    comment: Optional[str] = Field(default=None)
