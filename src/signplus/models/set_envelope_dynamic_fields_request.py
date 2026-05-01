from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .dynamic_fields import DynamicFields


class SetEnvelopeDynamicFieldsRequest(BaseModel):
    """SetEnvelopeDynamicFieldsRequest

    :param dynamic_fields: dynamic_fields, defaults to None
    :type dynamic_fields: List[DynamicFields], optional
    """

    dynamic_fields: Optional[List[DynamicFields]] = Field(default=None)
