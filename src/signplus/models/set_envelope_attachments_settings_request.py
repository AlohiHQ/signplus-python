from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .set_envelope_attachments_settings_request_settings import (
    SetEnvelopeAttachmentsSettingsRequestSettings,
)


class SetEnvelopeAttachmentsSettingsRequest(BaseModel):
    """SetEnvelopeAttachmentsSettingsRequest

    :param settings: settings, defaults to None
    :type settings: SetEnvelopeAttachmentsSettingsRequestSettings, optional
    """

    settings: Optional[SetEnvelopeAttachmentsSettingsRequestSettings] = Field(
        default=None
    )
