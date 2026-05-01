from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class SetEnvelopeAttachmentsSettingsRequestSettings(BaseModel):
    """SetEnvelopeAttachmentsSettingsRequestSettings

    :param visible_to_recipients: visible_to_recipients, defaults to None
    :type visible_to_recipients: bool, optional
    """

    visible_to_recipients: Optional[bool] = Field(default=None)
