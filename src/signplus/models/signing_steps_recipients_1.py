from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .verification import Verification


class SigningStepsRecipients1(BaseModel):
    """SigningStepsRecipients1

    :param name: name, defaults to None
    :type name: str, optional
    :param email: email, defaults to None
    :type email: str, optional
    :param role: role, defaults to None
    :type role: str, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param uid: uid, defaults to None
    :type uid: str, optional
    :param verification: verification, defaults to None
    :type verification: Verification, optional
    """

    name: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    role: Optional[str] = Field(default=None)
    id_: Optional[str] = Field(alias="id", serialization_alias="id", default=None)
    uid: Optional[str] = Field(default=None)
    verification: Optional[Verification] = Field(default=None)
