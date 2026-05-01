from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .add_envelope_annotation_request_signature import (
    AddEnvelopeAnnotationRequestSignature,
)
from .add_envelope_annotation_request_initials import (
    AddEnvelopeAnnotationRequestInitials,
)
from .add_envelope_annotation_request_text import AddEnvelopeAnnotationRequestText
from .add_envelope_annotation_request_datetime import (
    AddEnvelopeAnnotationRequestDatetime,
)
from .add_envelope_annotation_request_checkbox import (
    AddEnvelopeAnnotationRequestCheckbox,
)


class AddEnvelopeAnnotationRequest(BaseModel):
    """AddEnvelopeAnnotationRequest

    :param document_id: document_id, defaults to None
    :type document_id: str, optional
    :param page: page, defaults to None
    :type page: float, optional
    :param x: x, defaults to None
    :type x: float, optional
    :param y: y, defaults to None
    :type y: float, optional
    :param width: width, defaults to None
    :type width: float, optional
    :param height: height, defaults to None
    :type height: float, optional
    :param type_: type_, defaults to None
    :type type_: str, optional
    :param recipient_id: recipient_id, defaults to None
    :type recipient_id: str, optional
    :param required: required, defaults to None
    :type required: bool, optional
    :param signature: signature, defaults to None
    :type signature: AddEnvelopeAnnotationRequestSignature, optional
    :param initials: initials, defaults to None
    :type initials: AddEnvelopeAnnotationRequestInitials, optional
    :param text: text, defaults to None
    :type text: AddEnvelopeAnnotationRequestText, optional
    :param datetime_: datetime_, defaults to None
    :type datetime_: AddEnvelopeAnnotationRequestDatetime, optional
    :param checkbox: checkbox, defaults to None
    :type checkbox: AddEnvelopeAnnotationRequestCheckbox, optional
    """

    document_id: Optional[str] = Field(default=None)
    page: Optional[float] = Field(default=None)
    x: Optional[float] = Field(default=None)
    y: Optional[float] = Field(default=None)
    width: Optional[float] = Field(default=None)
    height: Optional[float] = Field(default=None)
    type_: Optional[str] = Field(alias="type", serialization_alias="type", default=None)
    recipient_id: Optional[str] = Field(default=None)
    required: Optional[bool] = Field(default=None)
    signature: Optional[AddEnvelopeAnnotationRequestSignature] = Field(default=None)
    initials: Optional[AddEnvelopeAnnotationRequestInitials] = Field(default=None)
    text: Optional[AddEnvelopeAnnotationRequestText] = Field(default=None)
    datetime_: Optional[AddEnvelopeAnnotationRequestDatetime] = Field(
        alias="datetime", serialization_alias="datetime", default=None
    )
    checkbox: Optional[AddEnvelopeAnnotationRequestCheckbox] = Field(default=None)
