from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .envelope_flow_type import EnvelopeFlowType
from .envelope_legality_level import EnvelopeLegalityLevel
from .envelope_status import EnvelopeStatus
from .signing_step import SigningStep
from .document import Document
from .envelope_notification import EnvelopeNotification
from .envelope_attachments import EnvelopeAttachments


class Envelope(BaseModel):
    """Envelope

    :param id_: Unique identifier of the envelope, defaults to None
    :type id_: str, optional
    :param name: Name of the envelope, defaults to None
    :type name: str, optional
    :param comment: Comment for the envelope, defaults to None
    :type comment: str, optional
    :param pages: Total number of pages in the envelope, defaults to None
    :type pages: int, optional
    :param flow_type: Flow type of the envelope (REQUEST_SIGNATURE is a request for signature, SIGN_MYSELF is a self-signing flow), defaults to None
    :type flow_type: EnvelopeFlowType, optional
    :param legality_level: Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes), defaults to None
    :type legality_level: EnvelopeLegalityLevel, optional
    :param status: Status of the envelope, defaults to None
    :type status: EnvelopeStatus, optional
    :param created_at: Unix timestamp of the creation date, defaults to None
    :type created_at: int, optional
    :param updated_at: Unix timestamp of the last modification date, defaults to None
    :type updated_at: int, optional
    :param expires_at: Unix timestamp of the expiration date, defaults to None
    :type expires_at: int, optional
    :param num_recipients: Number of recipients in the envelope, defaults to None
    :type num_recipients: int, optional
    :param is_duplicable: Whether the envelope can be duplicated, defaults to None
    :type is_duplicable: bool, optional
    :param signing_steps: signing_steps, defaults to None
    :type signing_steps: List[SigningStep], optional
    :param documents: documents, defaults to None
    :type documents: List[Document], optional
    :param notification: notification, defaults to None
    :type notification: EnvelopeNotification, optional
    :param attachments: attachments, defaults to None
    :type attachments: EnvelopeAttachments, optional
    """

    id_: Optional[str] = Field(
        alias="id",
        serialization_alias="id",
        default=None,
        description="Unique identifier of the envelope",
    )
    name: Optional[str] = Field(default=None, description="Name of the envelope")
    comment: Optional[str] = Field(default=None, description="Comment for the envelope")
    pages: Optional[int] = Field(
        default=None, description="Total number of pages in the envelope"
    )
    flow_type: Optional[EnvelopeFlowType] = Field(
        default=None,
        description="Flow type of the envelope (REQUEST_SIGNATURE is a request for signature, SIGN_MYSELF is a self-signing flow)",
    )
    legality_level: Optional[EnvelopeLegalityLevel] = Field(
        default=None,
        description="Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes)",
    )
    status: Optional[EnvelopeStatus] = Field(
        default=None, description="Status of the envelope"
    )
    created_at: Optional[int] = Field(
        default=None, description="Unix timestamp of the creation date"
    )
    updated_at: Optional[int] = Field(
        default=None, description="Unix timestamp of the last modification date"
    )
    expires_at: Optional[int] = Field(
        default=None, description="Unix timestamp of the expiration date"
    )
    num_recipients: Optional[int] = Field(
        default=None, description="Number of recipients in the envelope"
    )
    is_duplicable: Optional[bool] = Field(
        default=None, description="Whether the envelope can be duplicated"
    )
    signing_steps: Optional[List[SigningStep]] = Field(default=None)
    documents: Optional[List[Document]] = Field(default=None)
    notification: Optional[EnvelopeNotification] = Field(default=None)
    attachments: Optional[EnvelopeAttachments] = Field(default=None)
