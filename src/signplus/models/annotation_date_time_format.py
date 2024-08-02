from enum import Enum


class AnnotationDateTimeFormat(Enum):
    """An enumeration representing different categories.

    :cvar DMY_NUMERIC_SLASH: "DMY_NUMERIC_SLASH"
    :vartype DMY_NUMERIC_SLASH: str
    :cvar MDY_NUMERIC_SLASH: "MDY_NUMERIC_SLASH"
    :vartype MDY_NUMERIC_SLASH: str
    :cvar YMD_NUMERIC_SLASH: "YMD_NUMERIC_SLASH"
    :vartype YMD_NUMERIC_SLASH: str
    :cvar DMY_NUMERIC_DASH_SHORT: "DMY_NUMERIC_DASH_SHORT"
    :vartype DMY_NUMERIC_DASH_SHORT: str
    :cvar DMY_NUMERIC_DASH: "DMY_NUMERIC_DASH"
    :vartype DMY_NUMERIC_DASH: str
    :cvar YMD_NUMERIC_DASH: "YMD_NUMERIC_DASH"
    :vartype YMD_NUMERIC_DASH: str
    :cvar MDY_TEXT_DASH_SHORT: "MDY_TEXT_DASH_SHORT"
    :vartype MDY_TEXT_DASH_SHORT: str
    :cvar MDY_TEXT_SPACE_SHORT: "MDY_TEXT_SPACE_SHORT"
    :vartype MDY_TEXT_SPACE_SHORT: str
    :cvar MDY_TEXT_SPACE: "MDY_TEXT_SPACE"
    :vartype MDY_TEXT_SPACE: str
    """

    DMY_NUMERIC_SLASH = "DMY_NUMERIC_SLASH"
    MDY_NUMERIC_SLASH = "MDY_NUMERIC_SLASH"
    YMD_NUMERIC_SLASH = "YMD_NUMERIC_SLASH"
    DMY_NUMERIC_DASH_SHORT = "DMY_NUMERIC_DASH_SHORT"
    DMY_NUMERIC_DASH = "DMY_NUMERIC_DASH"
    YMD_NUMERIC_DASH = "YMD_NUMERIC_DASH"
    MDY_TEXT_DASH_SHORT = "MDY_TEXT_DASH_SHORT"
    MDY_TEXT_SPACE_SHORT = "MDY_TEXT_SPACE_SHORT"
    MDY_TEXT_SPACE = "MDY_TEXT_SPACE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, AnnotationDateTimeFormat._member_map_.values())
        )
