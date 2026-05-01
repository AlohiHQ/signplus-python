from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class AddTemplateAnnotationRequestSignature(BaseModel):
    """AddTemplateAnnotationRequestSignature

    :param id_: id_, defaults to None
    :type id_: str, optional
    """

    id_: Optional[str] = Field(alias="id", serialization_alias="id", default=None)
