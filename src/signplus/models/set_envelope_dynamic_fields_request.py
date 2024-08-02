from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .dynamic_field import DynamicField


@JsonMap({})
class SetEnvelopeDynamicFieldsRequest(BaseModel):
    """SetEnvelopeDynamicFieldsRequest

    :param dynamic_fields: List of dynamic fields, defaults to None
    :type dynamic_fields: List[DynamicField], optional
    """

    def __init__(self, dynamic_fields: List[DynamicField] = None):
        """SetEnvelopeDynamicFieldsRequest

        :param dynamic_fields: List of dynamic fields, defaults to None
        :type dynamic_fields: List[DynamicField], optional
        """
        if dynamic_fields is not None:
            self.dynamic_fields = self._define_list(dynamic_fields, DynamicField)
