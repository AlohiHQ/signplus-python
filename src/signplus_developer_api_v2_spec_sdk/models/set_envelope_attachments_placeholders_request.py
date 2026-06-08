from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel
from .attachment_placeholder_request import AttachmentPlaceholderRequest


class SetEnvelopeAttachmentsPlaceholdersRequest(BaseModel):
    """SetEnvelopeAttachmentsPlaceholdersRequest

    :param placeholders: placeholders
    :type placeholders: List[AttachmentPlaceholderRequest]
    """

    placeholders: List[AttachmentPlaceholderRequest]
