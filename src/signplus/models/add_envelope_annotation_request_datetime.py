from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .datetime_font_1 import DatetimeFont1


class AddEnvelopeAnnotationRequestDatetime(BaseModel):
    """AddEnvelopeAnnotationRequestDatetime

    :param size: size, defaults to None
    :type size: str, optional
    :param font: font, defaults to None
    :type font: DatetimeFont1, optional
    :param color: color, defaults to None
    :type color: str, optional
    :param auto_fill: auto_fill, defaults to None
    :type auto_fill: str, optional
    :param timezone: timezone, defaults to None
    :type timezone: str, optional
    :param timestamp: timestamp, defaults to None
    :type timestamp: str, optional
    :param format: format, defaults to None
    :type format: str, optional
    """

    size: Optional[str] = Field(default=None)
    font: Optional[DatetimeFont1] = Field(default=None)
    color: Optional[str] = Field(default=None)
    auto_fill: Optional[str] = Field(default=None)
    timezone: Optional[str] = Field(default=None)
    timestamp: Optional[str] = Field(default=None)
    format: Optional[str] = Field(default=None)
