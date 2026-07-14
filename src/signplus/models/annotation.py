from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .annotation_type import AnnotationType
from .annotation_signature import AnnotationSignature
from .annotation_initials import AnnotationInitials
from .annotation_text import AnnotationText
from .annotation_date_time import AnnotationDateTime
from .annotation_checkbox import AnnotationCheckbox


class Annotation(BaseModel):
    """Annotation

    :param id_: Unique identifier of the annotation, defaults to None
    :type id_: str, optional
    :param recipient_id: ID of the recipient, defaults to None
    :type recipient_id: str, optional
    :param document_id: ID of the document, defaults to None
    :type document_id: str, optional
    :param page: Page number where the annotation is placed, defaults to None
    :type page: int, optional
    :param x: X coordinate of the annotation (in % of the page width from 0 to 100) from the top left corner, defaults to None
    :type x: float, optional
    :param y: Y coordinate of the annotation (in % of the page height from 0 to 100) from the top left corner, defaults to None
    :type y: float, optional
    :param width: Width of the annotation (in % of the page width from 0 to 100), defaults to None
    :type width: float, optional
    :param height: Height of the annotation (in % of the page height from 0 to 100), defaults to None
    :type height: float, optional
    :param required: Whether the annotation is required, defaults to None
    :type required: bool, optional
    :param type_: Type of the annotation, defaults to None
    :type type_: AnnotationType, optional
    :param signature: Signature annotation (null if annotation is not a signature), defaults to None
    :type signature: AnnotationSignature, optional
    :param initials: Initials annotation (null if annotation is not initials), defaults to None
    :type initials: AnnotationInitials, optional
    :param text: Text annotation (null if annotation is not a text), defaults to None
    :type text: AnnotationText, optional
    :param datetime_: Date annotation (null if annotation is not a date), defaults to None
    :type datetime_: AnnotationDateTime, optional
    :param checkbox: Checkbox annotation (null if annotation is not a checkbox), defaults to None
    :type checkbox: AnnotationCheckbox, optional
    """

    id_: Optional[str] = Field(
        alias="id",
        serialization_alias="id",
        default=None,
        description="Unique identifier of the annotation",
    )
    recipient_id: Optional[str] = Field(default=None, description="ID of the recipient")
    document_id: Optional[str] = Field(default=None, description="ID of the document")
    page: Optional[int] = Field(
        default=None, description="Page number where the annotation is placed"
    )
    x: Optional[float] = Field(
        default=None,
        description="X coordinate of the annotation (in % of the page width from 0 to 100) from the top left corner",
    )
    y: Optional[float] = Field(
        default=None,
        description="Y coordinate of the annotation (in % of the page height from 0 to 100) from the top left corner",
    )
    width: Optional[float] = Field(
        default=None,
        description="Width of the annotation (in % of the page width from 0 to 100)",
    )
    height: Optional[float] = Field(
        default=None,
        description="Height of the annotation (in % of the page height from 0 to 100)",
    )
    required: Optional[bool] = Field(
        default=None, description="Whether the annotation is required"
    )
    type_: Optional[AnnotationType] = Field(
        alias="type",
        serialization_alias="type",
        default=None,
        description="Type of the annotation",
    )
    signature: Optional[AnnotationSignature] = Field(
        default=None,
        description="Signature annotation (null if annotation is not a signature)",
    )
    initials: Optional[AnnotationInitials] = Field(
        default=None,
        description="Initials annotation (null if annotation is not initials)",
    )
    text: Optional[AnnotationText] = Field(
        default=None, description="Text annotation (null if annotation is not a text)"
    )
    datetime_: Optional[AnnotationDateTime] = Field(
        alias="datetime",
        serialization_alias="datetime",
        default=None,
        description="Date annotation (null if annotation is not a date)",
    )
    checkbox: Optional[AnnotationCheckbox] = Field(
        default=None,
        description="Checkbox annotation (null if annotation is not a checkbox)",
    )
