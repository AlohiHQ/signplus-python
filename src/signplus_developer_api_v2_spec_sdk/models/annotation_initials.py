from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel


class AnnotationInitials(BaseModel):
    """Initials annotation (null if annotation is not initials)

    :param id_: Unique identifier of the annotation initials, defaults to None
    :type id_: str, optional
    """

    id_: Optional[str] = Field(
        alias="id",
        serialization_alias="id",
        default=None,
        description="Unique identifier of the annotation initials",
    )
