from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .template import Template


class ListTemplatesResponse(BaseModel):
    """ListTemplatesResponse

    :param has_next_page: Whether there is a next page, defaults to None
    :type has_next_page: bool, optional
    :param has_previous_page: Whether there is a previous page, defaults to None
    :type has_previous_page: bool, optional
    :param templates: templates, defaults to None
    :type templates: List[Template], optional
    """

    has_next_page: Optional[bool] = Field(
        default=None, description="Whether there is a next page"
    )
    has_previous_page: Optional[bool] = Field(
        default=None, description="Whether there is a previous page"
    )
    templates: Optional[List[Template]] = Field(default=None)
