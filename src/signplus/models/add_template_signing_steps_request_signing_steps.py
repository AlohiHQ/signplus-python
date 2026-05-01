from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .signing_steps_recipients_2 import SigningStepsRecipients2


class AddTemplateSigningStepsRequestSigningSteps(BaseModel):
    """AddTemplateSigningStepsRequestSigningSteps

    :param recipients: recipients, defaults to None
    :type recipients: List[SigningStepsRecipients2], optional
    """

    recipients: Optional[List[SigningStepsRecipients2]] = Field(default=None)
