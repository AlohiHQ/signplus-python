from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .add_template_signing_steps_request_signing_steps import (
    AddTemplateSigningStepsRequestSigningSteps,
)


class AddTemplateSigningStepsRequest(BaseModel):
    """AddTemplateSigningStepsRequest

    :param signing_steps: signing_steps, defaults to None
    :type signing_steps: List[AddTemplateSigningStepsRequestSigningSteps], optional
    """

    signing_steps: Optional[List[AddTemplateSigningStepsRequestSigningSteps]] = Field(
        default=None
    )
