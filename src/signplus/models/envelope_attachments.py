from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .attachment_settings import AttachmentSettings
from .attachment_placeholders_per_recipient import AttachmentPlaceholdersPerRecipient


class EnvelopeAttachments(BaseModel):
    """EnvelopeAttachments

    :param settings: settings, defaults to None
    :type settings: AttachmentSettings, optional
    :param recipients: recipients, defaults to None
    :type recipients: List[AttachmentPlaceholdersPerRecipient], optional
    """

    settings: Optional[AttachmentSettings] = Field(default=None)
    recipients: Optional[List[AttachmentPlaceholdersPerRecipient]] = Field(default=None)
