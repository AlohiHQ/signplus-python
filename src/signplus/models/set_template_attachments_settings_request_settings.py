from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class SetTemplateAttachmentsSettingsRequestSettings(BaseModel):
    """SetTemplateAttachmentsSettingsRequestSettings

    :param visible_to_recipients: visible_to_recipients, defaults to None
    :type visible_to_recipients: str, optional
    """

    visible_to_recipients: Optional[str] = Field(default=None)
