from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class RenameTemplateRequest(BaseModel):
    """RenameTemplateRequest

    :param name: Name of the template
    :type name: str
    """

    name: str = Field(description="Name of the template")
