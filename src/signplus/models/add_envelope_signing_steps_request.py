from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .add_envelope_signing_steps_request_signing_steps import (
    AddEnvelopeSigningStepsRequestSigningSteps,
)


class AddEnvelopeSigningStepsRequest(BaseModel):
    """AddEnvelopeSigningStepsRequest

    :param signing_steps: signing_steps, defaults to None
    :type signing_steps: List[AddEnvelopeSigningStepsRequestSigningSteps], optional
    """

    signing_steps: Optional[List[AddEnvelopeSigningStepsRequestSigningSteps]] = Field(
        default=None
    )
