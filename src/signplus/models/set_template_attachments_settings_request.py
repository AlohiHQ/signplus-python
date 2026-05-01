from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .set_template_attachments_settings_request_settings import (
    SetTemplateAttachmentsSettingsRequestSettings,
)


class SetTemplateAttachmentsSettingsRequest(BaseModel):
    """SetTemplateAttachmentsSettingsRequest

    :param settings: settings, defaults to None
    :type settings: SetTemplateAttachmentsSettingsRequestSettings, optional
    """

    settings: Optional[SetTemplateAttachmentsSettingsRequestSettings] = Field(
        default=None
    )
