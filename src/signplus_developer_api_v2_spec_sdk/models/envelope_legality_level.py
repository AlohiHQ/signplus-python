from enum import Enum


class EnvelopeLegalityLevel(str, Enum):
    """An enumeration representing different categories.

    :cvar SES: "SES"
    :vartype SES: str
    :cvar QESEIDAS: "QES_EIDAS"
    :vartype QESEIDAS: str
    :cvar QESZERTES: "QES_ZERTES"
    :vartype QESZERTES: str
    """

    SES = "SES"
    QESEIDAS = "QES_EIDAS"
    QESZERTES = "QES_ZERTES"

    @staticmethod
    def list():
        """Lists all enum values.

        :return: A list of all enum values.
        :rtype: list
        """
        return list(map(lambda x: x.value, EnvelopeLegalityLevel._member_map_.values()))
