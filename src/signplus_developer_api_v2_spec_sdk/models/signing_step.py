from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel
from .recipient import Recipient


class SigningStep(BaseModel):
    """SigningStep

    :param recipients: List of recipients, defaults to None
    :type recipients: List[Recipient], optional
    """

    recipients: Optional[List[Recipient]] = Field(
        default=None, description="List of recipients"
    )
