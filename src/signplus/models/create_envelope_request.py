from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class CreateEnvelopeRequest(BaseModel):
    """CreateEnvelopeRequest

    :param name: name, defaults to None
    :type name: str, optional
    :param legality_level: legality_level, defaults to None
    :type legality_level: str, optional
    :param expires_at: expires_at, defaults to None
    :type expires_at: float, optional
    :param comment: comment, defaults to None
    :type comment: str, optional
    :param sandbox: sandbox, defaults to None
    :type sandbox: bool, optional
    """

    name: Optional[str] = Field(default=None)
    legality_level: Optional[str] = Field(default=None)
    expires_at: Optional[float] = Field(default=None)
    comment: Optional[str] = Field(default=None)
    sandbox: Optional[bool] = Field(default=None)
