from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .text_font_1 import TextFont1


class AddEnvelopeAnnotationRequestText(BaseModel):
    """AddEnvelopeAnnotationRequestText

    :param size: size, defaults to None
    :type size: float, optional
    :param color: color, defaults to None
    :type color: float, optional
    :param value: value, defaults to None
    :type value: str, optional
    :param tooltip: tooltip, defaults to None
    :type tooltip: str, optional
    :param dynamic_field_name: dynamic_field_name, defaults to None
    :type dynamic_field_name: str, optional
    :param font: font, defaults to None
    :type font: TextFont1, optional
    """

    size: Optional[float] = Field(default=None)
    color: Optional[float] = Field(default=None)
    value: Optional[str] = Field(default=None)
    tooltip: Optional[str] = Field(default=None)
    dynamic_field_name: Optional[str] = Field(default=None)
    font: Optional[TextFont1] = Field(default=None)
