from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class DynamicField(BaseModel):
    """DynamicField

    :param name: Name of the dynamic field, defaults to None
    :type name: str, optional
    :param value: Value of the dynamic field, defaults to None
    :type value: str, optional
    """

    name: Optional[str] = Field(default=None, description="Name of the dynamic field")
    value: Optional[str] = Field(default=None, description="Value of the dynamic field")
