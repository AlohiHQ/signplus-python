from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .set_envelope_attachments_placeholders_request_placeholders import (
    SetEnvelopeAttachmentsPlaceholdersRequestPlaceholders,
)


class SetEnvelopeAttachmentsPlaceholdersRequest(BaseModel):
    """SetEnvelopeAttachmentsPlaceholdersRequest

    :param placeholders: placeholders, defaults to None
    :type placeholders: List[SetEnvelopeAttachmentsPlaceholdersRequestPlaceholders], optional
    """

    placeholders: Optional[
        List[SetEnvelopeAttachmentsPlaceholdersRequestPlaceholders]
    ] = Field(default=None)
