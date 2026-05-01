from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .add_template_annotation_request_signature import (
    AddTemplateAnnotationRequestSignature,
)
from .add_template_annotation_request_initials import (
    AddTemplateAnnotationRequestInitials,
)
from .add_template_annotation_request_text import AddTemplateAnnotationRequestText
from .add_template_annotation_request_datetime import (
    AddTemplateAnnotationRequestDatetime,
)
from .add_template_annotation_request_checkbox import (
    AddTemplateAnnotationRequestCheckbox,
)


class AddTemplateAnnotationRequest(BaseModel):
    """AddTemplateAnnotationRequest

    :param document_id: document_id, defaults to None
    :type document_id: str, optional
    :param page: page, defaults to None
    :type page: str, optional
    :param x: x, defaults to None
    :type x: str, optional
    :param y: y, defaults to None
    :type y: str, optional
    :param width: width, defaults to None
    :type width: str, optional
    :param height: height, defaults to None
    :type height: str, optional
    :param type_: type_, defaults to None
    :type type_: str, optional
    :param recipient_id: recipient_id, defaults to None
    :type recipient_id: str, optional
    :param required: required, defaults to None
    :type required: str, optional
    :param signature: signature, defaults to None
    :type signature: AddTemplateAnnotationRequestSignature, optional
    :param initials: initials, defaults to None
    :type initials: AddTemplateAnnotationRequestInitials, optional
    :param text: text, defaults to None
    :type text: AddTemplateAnnotationRequestText, optional
    :param datetime_: datetime_, defaults to None
    :type datetime_: AddTemplateAnnotationRequestDatetime, optional
    :param checkbox: checkbox, defaults to None
    :type checkbox: AddTemplateAnnotationRequestCheckbox, optional
    """

    document_id: Optional[str] = Field(default=None)
    page: Optional[str] = Field(default=None)
    x: Optional[str] = Field(default=None)
    y: Optional[str] = Field(default=None)
    width: Optional[str] = Field(default=None)
    height: Optional[str] = Field(default=None)
    type_: Optional[str] = Field(alias="type", serialization_alias="type", default=None)
    recipient_id: Optional[str] = Field(default=None)
    required: Optional[str] = Field(default=None)
    signature: Optional[AddTemplateAnnotationRequestSignature] = Field(default=None)
    initials: Optional[AddTemplateAnnotationRequestInitials] = Field(default=None)
    text: Optional[AddTemplateAnnotationRequestText] = Field(default=None)
    datetime_: Optional[AddTemplateAnnotationRequestDatetime] = Field(
        alias="datetime", serialization_alias="datetime", default=None
    )
    checkbox: Optional[AddTemplateAnnotationRequestCheckbox] = Field(default=None)
