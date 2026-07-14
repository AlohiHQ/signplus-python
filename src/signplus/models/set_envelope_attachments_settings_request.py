from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .attachment_settings import AttachmentSettings


class SetEnvelopeAttachmentsSettingsRequest(BaseModel):
    """SetEnvelopeAttachmentsSettingsRequest

    :param settings: settings
    :type settings: AttachmentSettings
    """

    settings: AttachmentSettings
