from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class SetTemplateAttachmentsPlaceholdersRequestPlaceholders(BaseModel):
    """SetTemplateAttachmentsPlaceholdersRequestPlaceholders

    :param recipient_id: recipient_id, defaults to None
    :type recipient_id: str, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param required: required, defaults to None
    :type required: str, optional
    :param multiple: multiple, defaults to None
    :type multiple: str, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param hint: hint, defaults to None
    :type hint: str, optional
    """

    recipient_id: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    required: Optional[str] = Field(default=None)
    multiple: Optional[str] = Field(default=None)
    id_: Optional[str] = Field(alias="id", serialization_alias="id", default=None)
    hint: Optional[str] = Field(default=None)
