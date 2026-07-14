from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SetTemplateCommentRequest(BaseModel):
    """SetTemplateCommentRequest

    :param comment: Comment for the template
    :type comment: str
    """

    comment: str = Field(description="Comment for the template")
