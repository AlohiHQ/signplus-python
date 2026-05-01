from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .signing_steps_recipients_1 import SigningStepsRecipients1


class AddEnvelopeSigningStepsRequestSigningSteps(BaseModel):
    """AddEnvelopeSigningStepsRequestSigningSteps

    :param recipients: recipients, defaults to None
    :type recipients: List[SigningStepsRecipients1], optional
    """

    recipients: Optional[List[SigningStepsRecipients1]] = Field(default=None)
