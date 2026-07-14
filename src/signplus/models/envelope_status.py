from __future__ import annotations
from enum import Enum
from typing import Any


class EnvelopeStatus(str, Enum):
    """An enumeration representing different categories.

    :cvar DRAFT: "DRAFT"
    :vartype DRAFT: str
    :cvar INPROGRESS: "IN_PROGRESS"
    :vartype INPROGRESS: str
    :cvar COMPLETED: "COMPLETED"
    :vartype COMPLETED: str
    :cvar EXPIRED: "EXPIRED"
    :vartype EXPIRED: str
    :cvar DECLINED: "DECLINED"
    :vartype DECLINED: str
    :cvar VOIDED: "VOIDED"
    :vartype VOIDED: str
    :cvar PENDING: "PENDING"
    :vartype PENDING: str
    """

    DRAFT = "DRAFT"
    INPROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    EXPIRED = "EXPIRED"
    DECLINED = "DECLINED"
    VOIDED = "VOIDED"
    PENDING = "PENDING"

    @staticmethod
    def list():
        """Lists all enum values.

        :return: A list of all enum values.
        :rtype: list
        """
        return list(map(lambda x: x.value, EnvelopeStatus._member_map_.values()))
