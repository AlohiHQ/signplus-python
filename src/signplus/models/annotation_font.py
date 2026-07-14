from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .annotation_font_family import AnnotationFontFamily


class AnnotationFont(BaseModel):
    """AnnotationFont

    :param family: Font family of the text, defaults to None
    :type family: AnnotationFontFamily, optional
    :param italic: Whether the text is italic, defaults to None
    :type italic: bool, optional
    :param bold: Whether the text is bold, defaults to None
    :type bold: bool, optional
    """

    family: Optional[AnnotationFontFamily] = Field(
        default=None, description="Font family of the text"
    )
    italic: Optional[bool] = Field(
        default=None, description="Whether the text is italic"
    )
    bold: Optional[bool] = Field(default=None, description="Whether the text is bold")
