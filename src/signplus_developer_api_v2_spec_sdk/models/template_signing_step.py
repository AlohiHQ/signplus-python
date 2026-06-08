from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel
from .template_recipient import TemplateRecipient


class TemplateSigningStep(BaseModel):
    """TemplateSigningStep

    :param recipients: List of recipients, defaults to None
    :type recipients: List[TemplateRecipient], optional
    """

    recipients: Optional[List[TemplateRecipient]] = Field(
        default=None, description="List of recipients"
    )
