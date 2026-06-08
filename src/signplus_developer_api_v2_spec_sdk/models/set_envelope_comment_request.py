from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class SetEnvelopeCommentRequest(BaseModel):
    """SetEnvelopeCommentRequest

    :param comment: Comment for the envelope
    :type comment: str
    """

    comment: str = Field(description="Comment for the envelope")
