from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class CreateEnvelopeFromTemplateRequest(BaseModel):
    """CreateEnvelopeFromTemplateRequest

    :param name: name, defaults to None
    :type name: str, optional
    :param comment: comment, defaults to None
    :type comment: str, optional
    :param sandbox: sandbox, defaults to None
    :type sandbox: bool, optional
    """

    name: Optional[str] = Field(default=None)
    comment: Optional[str] = Field(default=None)
    sandbox: Optional[bool] = Field(default=None)
