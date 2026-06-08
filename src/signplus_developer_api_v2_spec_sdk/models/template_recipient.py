from __future__ import annotations
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel
from .template_recipient_role import TemplateRecipientRole


class TemplateRecipient(BaseModel):
    """TemplateRecipient

    :param id_: Unique identifier of the recipient, defaults to None
    :type id_: str, optional
    :param uid: Unique identifier of the user associated with the recipient, defaults to None
    :type uid: str, optional
    :param name: Name of the recipient, defaults to None
    :type name: str, optional
    :param email: Email of the recipient, defaults to None
    :type email: str, optional
    :param role: Role of the recipient (SIGNER signs the document, RECEIVES_COPY receives a copy of the document, IN_PERSON_SIGNER signs the document in person, SENDER sends the document), defaults to None
    :type role: TemplateRecipientRole, optional
    """

    id_: Optional[str] = Field(
        alias="id",
        serialization_alias="id",
        default=None,
        description="Unique identifier of the recipient",
    )
    uid: Optional[str] = Field(
        default=None,
        description="Unique identifier of the user associated with the recipient",
    )
    name: Optional[str] = Field(default=None, description="Name of the recipient")
    email: Optional[str] = Field(default=None, description="Email of the recipient")
    role: Optional[TemplateRecipientRole] = Field(
        default=None,
        description="Role of the recipient (SIGNER signs the document, RECEIVES_COPY receives a copy of the document, IN_PERSON_SIGNER signs the document in person, SENDER sends the document)",
    )
