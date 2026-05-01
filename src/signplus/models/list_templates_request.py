from typing import List
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class ListTemplatesRequest(BaseModel):
    """ListTemplatesRequest

    :param name: name, defaults to None
    :type name: str, optional
    :param tags: tags, defaults to None
    :type tags: List[str], optional
    :param ids: ids, defaults to None
    :type ids: List[str], optional
    :param first: first, defaults to None
    :type first: float, optional
    :param last: last, defaults to None
    :type last: float, optional
    :param after: after, defaults to None
    :type after: str, optional
    :param before: before, defaults to None
    :type before: str, optional
    :param order_field: order_field, defaults to None
    :type order_field: str, optional
    :param ascending: ascending, defaults to None
    :type ascending: bool, optional
    """

    name: Optional[str] = Field(default=None)
    tags: Optional[List[str]] = Field(default=None)
    ids: Optional[List[str]] = Field(default=None)
    first: Optional[float] = Field(default=None)
    last: Optional[float] = Field(default=None)
    after: Optional[str] = Field(default=None)
    before: Optional[str] = Field(default=None)
    order_field: Optional[str] = Field(default=None)
    ascending: Optional[bool] = Field(default=None)
