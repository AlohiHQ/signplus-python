from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class Page(BaseModel):
    """Page

    :param width: Width of the page in pixels, defaults to None
    :type width: int, optional
    :param height: Height of the page in pixels, defaults to None
    :type height: int, optional
    """

    width: Optional[int] = Field(
        default=None, description="Width of the page in pixels"
    )
    height: Optional[int] = Field(
        default=None, description="Height of the page in pixels"
    )
