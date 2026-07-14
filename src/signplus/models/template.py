from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .envelope_legality_level import EnvelopeLegalityLevel
from .template_signing_step import TemplateSigningStep
from .document import Document
from .envelope_notification import EnvelopeNotification
from .envelope_attachments import EnvelopeAttachments


class Template(BaseModel):
    """Template

    :param id_: Unique identifier of the template, defaults to None
    :type id_: str, optional
    :param name: Name of the template, defaults to None
    :type name: str, optional
    :param comment: Comment for the template, defaults to None
    :type comment: str, optional
    :param pages: Total number of pages in the template, defaults to None
    :type pages: int, optional
    :param legality_level: Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes), defaults to None
    :type legality_level: EnvelopeLegalityLevel, optional
    :param created_at: Unix timestamp of the creation date, defaults to None
    :type created_at: int, optional
    :param updated_at: Unix timestamp of the last modification date, defaults to None
    :type updated_at: int, optional
    :param expiration_delay: Expiration delay added to the current time when an envelope is created from this template, defaults to None
    :type expiration_delay: int, optional
    :param num_recipients: Number of recipients in the envelope, defaults to None
    :type num_recipients: int, optional
    :param signing_steps: signing_steps, defaults to None
    :type signing_steps: List[TemplateSigningStep], optional
    :param documents: documents, defaults to None
    :type documents: List[Document], optional
    :param notification: notification, defaults to None
    :type notification: EnvelopeNotification, optional
    :param dynamic_fields: List of dynamic fields, defaults to None
    :type dynamic_fields: List[str], optional
    :param attachments: attachments, defaults to None
    :type attachments: EnvelopeAttachments, optional
    """

    id_: Optional[str] = Field(
        alias="id",
        serialization_alias="id",
        default=None,
        description="Unique identifier of the template",
    )
    name: Optional[str] = Field(default=None, description="Name of the template")
    comment: Optional[str] = Field(default=None, description="Comment for the template")
    pages: Optional[int] = Field(
        default=None, description="Total number of pages in the template"
    )
    legality_level: Optional[EnvelopeLegalityLevel] = Field(
        default=None,
        description="Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes)",
    )
    created_at: Optional[int] = Field(
        default=None, description="Unix timestamp of the creation date"
    )
    updated_at: Optional[int] = Field(
        default=None, description="Unix timestamp of the last modification date"
    )
    expiration_delay: Optional[int] = Field(
        default=None,
        description="Expiration delay added to the current time when an envelope is created from this template",
    )
    num_recipients: Optional[int] = Field(
        default=None, description="Number of recipients in the envelope"
    )
    signing_steps: Optional[List[TemplateSigningStep]] = Field(default=None)
    documents: Optional[List[Document]] = Field(default=None)
    notification: Optional[EnvelopeNotification] = Field(default=None)
    dynamic_fields: Optional[List[str]] = Field(
        default=None, description="List of dynamic fields"
    )
    attachments: Optional[EnvelopeAttachments] = Field(default=None)
