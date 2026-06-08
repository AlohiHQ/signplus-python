from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel
from .template_signing_step import TemplateSigningStep


class AddTemplateSigningStepsRequest(BaseModel):
    """AddTemplateSigningStepsRequest

    :param signing_steps: List of signing steps
    :type signing_steps: List[TemplateSigningStep]
    """

    signing_steps: List[TemplateSigningStep] = Field(
        description="List of signing steps"
    )
