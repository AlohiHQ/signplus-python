from enum import Enum


class AnnotationCheckboxStyle(Enum):
    """An enumeration representing different categories.

    :cvar CIRCLE_CHECK: "CIRCLE_CHECK"
    :vartype CIRCLE_CHECK: str
    :cvar CIRCLE_FULL: "CIRCLE_FULL"
    :vartype CIRCLE_FULL: str
    :cvar SQUARE_CHECK: "SQUARE_CHECK"
    :vartype SQUARE_CHECK: str
    :cvar SQUARE_FULL: "SQUARE_FULL"
    :vartype SQUARE_FULL: str
    :cvar CHECK_MARK: "CHECK_MARK"
    :vartype CHECK_MARK: str
    :cvar TIMES_SQUARE: "TIMES_SQUARE"
    :vartype TIMES_SQUARE: str
    """

    CIRCLE_CHECK = "CIRCLE_CHECK"
    CIRCLE_FULL = "CIRCLE_FULL"
    SQUARE_CHECK = "SQUARE_CHECK"
    SQUARE_FULL = "SQUARE_FULL"
    CHECK_MARK = "CHECK_MARK"
    TIMES_SQUARE = "TIMES_SQUARE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, AnnotationCheckboxStyle._member_map_.values())
        )
