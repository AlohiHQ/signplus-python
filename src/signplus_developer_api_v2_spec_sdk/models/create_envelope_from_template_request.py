from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class CreateEnvelopeFromTemplateRequest(BaseModel):
    """CreateEnvelopeFromTemplateRequest

    :param name: Name of the envelope
    :type name: str
    :param comment: Comment for the envelope, defaults to None
    :type comment: str, optional
    :param sandbox: Whether the envelope is created in sandbox mode, defaults to None
    :type sandbox: bool, optional
    """

    name: str = Field(
        description="Name of the envelope",
        pattern=r"^[a-zA-Z0-9][a-zA-Z0-9 ]*[a-zA-Z0-9]$",
        min_length=2,
        max_length=256,
    )
    comment: Optional[str] = Field(default=None, description="Comment for the envelope")
    sandbox: Optional[bool] = Field(
        default=None, description="Whether the envelope is created in sandbox mode"
    )
