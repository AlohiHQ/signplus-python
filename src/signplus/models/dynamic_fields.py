from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class DynamicFields(BaseModel):
    """DynamicFields

    :param name: name, defaults to None
    :type name: str, optional
    :param value: value, defaults to None
    :type value: str, optional
    """

    name: Optional[str] = Field(default=None)
    value: Optional[str] = Field(default=None)
