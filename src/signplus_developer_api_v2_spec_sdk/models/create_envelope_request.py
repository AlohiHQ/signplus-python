from __future__ import annotations
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel
from .envelope_legality_level import EnvelopeLegalityLevel


class CreateEnvelopeRequest(BaseModel):
    """CreateEnvelopeRequest

    :param name: Name of the envelope
    :type name: str
    :param legality_level: Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes)
    :type legality_level: EnvelopeLegalityLevel
    :param expires_at: Unix timestamp of the expiration date, defaults to None
    :type expires_at: int, optional
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
    legality_level: EnvelopeLegalityLevel = Field(
        description="Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes)"
    )
    expires_at: Optional[int] = Field(
        default=None, description="Unix timestamp of the expiration date"
    )
    comment: Optional[str] = Field(default=None, description="Comment for the envelope")
    sandbox: Optional[bool] = Field(
        default=None, description="Whether the envelope is created in sandbox mode"
    )
