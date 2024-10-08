from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .signing_step import SigningStep


@JsonMap({})
class AddEnvelopeSigningStepsRequest(BaseModel):
    """AddEnvelopeSigningStepsRequest

    :param signing_steps: List of signing steps, defaults to None
    :type signing_steps: List[SigningStep], optional
    """

    def __init__(self, signing_steps: List[SigningStep] = None):
        """AddEnvelopeSigningStepsRequest

        :param signing_steps: List of signing steps, defaults to None
        :type signing_steps: List[SigningStep], optional
        """
        if signing_steps is not None:
            self.signing_steps = self._define_list(signing_steps, SigningStep)
