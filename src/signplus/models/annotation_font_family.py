from __future__ import annotations
from enum import Enum
from typing import Any


class AnnotationFontFamily(str, Enum):
    """An enumeration representing different categories.

    :cvar UNKNOWN: "UNKNOWN"
    :vartype UNKNOWN: str
    :cvar SERIF: "SERIF"
    :vartype SERIF: str
    :cvar SANS: "SANS"
    :vartype SANS: str
    :cvar MONO: "MONO"
    :vartype MONO: str
    """

    UNKNOWN = "UNKNOWN"
    SERIF = "SERIF"
    SANS = "SANS"
    MONO = "MONO"

    @staticmethod
    def list():
        """Lists all enum values.

        :return: A list of all enum values.
        :rtype: list
        """
        return list(map(lambda x: x.value, AnnotationFontFamily._member_map_.values()))
