from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .dynamic_field import DynamicField


class SetEnvelopeDynamicFieldsRequest(BaseModel):
    """SetEnvelopeDynamicFieldsRequest

    :param dynamic_fields: List of dynamic fields
    :type dynamic_fields: List[DynamicField]
    """

    dynamic_fields: List[DynamicField] = Field(description="List of dynamic fields")
