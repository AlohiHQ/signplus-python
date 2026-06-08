from __future__ import annotations
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel
from .annotation_font import AnnotationFont


class AnnotationText(BaseModel):
    """Text annotation (null if annotation is not a text)

    :param size: Font size of the text in pt, defaults to None
    :type size: float, optional
    :param color: Text color in 32bit representation, defaults to None
    :type color: float, optional
    :param value: Text content of the annotation, defaults to None
    :type value: str, optional
    :param tooltip: Tooltip of the annotation, defaults to None
    :type tooltip: str, optional
    :param dynamic_field_name: Name of the dynamic field, defaults to None
    :type dynamic_field_name: str, optional
    :param font: font, defaults to None
    :type font: AnnotationFont, optional
    """

    size: Optional[float] = Field(
        default=None, description="Font size of the text in pt"
    )
    color: Optional[float] = Field(
        default=None, description="Text color in 32bit representation"
    )
    value: Optional[str] = Field(
        default=None, description="Text content of the annotation"
    )
    tooltip: Optional[str] = Field(
        default=None, description="Tooltip of the annotation"
    )
    dynamic_field_name: Optional[str] = Field(
        default=None, description="Name of the dynamic field"
    )
    font: Optional[AnnotationFont] = Field(default=None)
