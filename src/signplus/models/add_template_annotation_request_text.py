from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .text_font_2 import TextFont2


class AddTemplateAnnotationRequestText(BaseModel):
    """AddTemplateAnnotationRequestText

    :param size: size, defaults to None
    :type size: str, optional
    :param color: color, defaults to None
    :type color: str, optional
    :param value: value, defaults to None
    :type value: str, optional
    :param tooltip: tooltip, defaults to None
    :type tooltip: str, optional
    :param dynamic_field_name: dynamic_field_name, defaults to None
    :type dynamic_field_name: str, optional
    :param font: font, defaults to None
    :type font: TextFont2, optional
    """

    size: Optional[str] = Field(default=None)
    color: Optional[str] = Field(default=None)
    value: Optional[str] = Field(default=None)
    tooltip: Optional[str] = Field(default=None)
    dynamic_field_name: Optional[str] = Field(default=None)
    font: Optional[TextFont2] = Field(default=None)
