from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class AttachmentSettings(BaseModel):
    """AttachmentSettings

    :param visible_to_recipients: Whether the attachment is visible to the recipients, defaults to None
    :type visible_to_recipients: bool, optional
    """

    visible_to_recipients: Optional[bool] = Field(
        default=None, description="Whether the attachment is visible to the recipients"
    )
