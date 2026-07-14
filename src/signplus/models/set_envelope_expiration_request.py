from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class SetEnvelopeExpirationRequest(BaseModel):
    """SetEnvelopeExpirationRequest

    :param expires_at: Unix timestamp of the expiration date
    :type expires_at: int
    """

    expires_at: int = Field(description="Unix timestamp of the expiration date")
