from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class SetEnvelopeExpirationDateRequest(BaseModel):
    """SetEnvelopeExpirationDateRequest

    :param expires_at: expires_at, defaults to None
    :type expires_at: str, optional
    """

    expires_at: Optional[str] = Field(default=None)
