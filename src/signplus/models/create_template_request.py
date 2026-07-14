from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class CreateTemplateRequest(BaseModel):
    """CreateTemplateRequest

    :param name: name
    :type name: str
    """

    name: str = Field(
        pattern=r"^[a-zA-Z0-9][a-zA-Z0-9 ]*[a-zA-Z0-9]$", min_length=2, max_length=256
    )
