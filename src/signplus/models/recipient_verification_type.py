from __future__ import annotations
from enum import Enum
from typing import Any


class RecipientVerificationType(str, Enum):
    """An enumeration representing different categories.

    :cvar SMS: "SMS"
    :vartype SMS: str
    :cvar PASSCODE: "PASSCODE"
    :vartype PASSCODE: str
    :cvar IDVERIFICATION: "ID_VERIFICATION"
    :vartype IDVERIFICATION: str
    """

    SMS = "SMS"
    PASSCODE = "PASSCODE"
    IDVERIFICATION = "ID_VERIFICATION"

    @staticmethod
    def list():
        """Lists all enum values.

        :return: A list of all enum values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, RecipientVerificationType._member_map_.values())
        )
