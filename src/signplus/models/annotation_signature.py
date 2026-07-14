from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel


class AnnotationSignature(BaseModel):
    """Signature annotation (null if annotation is not a signature)

    :param id_: Unique identifier of the annotation signature, defaults to None
    :type id_: str, optional
    """

    id_: Optional[str] = Field(
        alias="id",
        serialization_alias="id",
        default=None,
        description="Unique identifier of the annotation signature",
    )
