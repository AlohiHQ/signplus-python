from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class Verification(BaseModel):
    """Verification

    :param type_: type_, defaults to None
    :type type_: str, optional
    :param value: value, defaults to None
    :type value: str, optional
    """

    type_: Optional[str] = Field(alias="type", serialization_alias="type", default=None)
    value: Optional[str] = Field(default=None)
