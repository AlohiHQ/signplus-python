from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .envelope_legality_level import EnvelopeLegalityLevel


class SetEnvelopeLegalityLevelRequest(BaseModel):
    """SetEnvelopeLegalityLevelRequest

    :param legality_level: Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes), defaults to None
    :type legality_level: EnvelopeLegalityLevel, optional
    """

    legality_level: Optional[EnvelopeLegalityLevel] = Field(
        default=None,
        description="Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes)",
    )
