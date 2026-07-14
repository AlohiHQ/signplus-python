from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .signing_step import SigningStep


class AddEnvelopeSigningStepsRequest(BaseModel):
    """AddEnvelopeSigningStepsRequest

    :param signing_steps: List of signing steps, defaults to None
    :type signing_steps: List[SigningStep], optional
    """

    signing_steps: Optional[List[SigningStep]] = Field(
        default=None, description="List of signing steps"
    )
