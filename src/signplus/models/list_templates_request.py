from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .template_order_field import TemplateOrderField


class ListTemplatesRequest(BaseModel):
    """ListTemplatesRequest

    :param name: Name of the template, defaults to None
    :type name: str, optional
    :param tags: List of tag templates, defaults to None
    :type tags: List[str], optional
    :param ids: List of templates IDs, defaults to None
    :type ids: List[str], optional
    :param first: first, defaults to None
    :type first: int, optional
    :param last: last, defaults to None
    :type last: int, optional
    :param after: after, defaults to None
    :type after: str, optional
    :param before: before, defaults to None
    :type before: str, optional
    :param order_field: Field to order templates by, defaults to None
    :type order_field: TemplateOrderField, optional
    :param ascending: Whether to order templates in ascending order, defaults to None
    :type ascending: bool, optional
    """

    name: Optional[str] = Field(default=None, description="Name of the template")
    tags: Optional[List[str]] = Field(default=None, description="List of tag templates")
    ids: Optional[List[str]] = Field(default=None, description="List of templates IDs")
    first: Optional[int] = Field(default=None)
    last: Optional[int] = Field(default=None)
    after: Optional[str] = Field(default=None)
    before: Optional[str] = Field(default=None)
    order_field: Optional[TemplateOrderField] = Field(
        default=None, description="Field to order templates by"
    )
    ascending: Optional[bool] = Field(
        default=None, description="Whether to order templates in ascending order"
    )
