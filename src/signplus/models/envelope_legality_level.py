from enum import Enum


class EnvelopeLegalityLevel(Enum):
    """An enumeration representing different categories.

    :cvar SES: "SES"
    :vartype SES: str
    :cvar QES_EIDAS: "QES_EIDAS"
    :vartype QES_EIDAS: str
    :cvar QES_ZERTES: "QES_ZERTES"
    :vartype QES_ZERTES: str
    """

    SES = "SES"
    QES_EIDAS = "QES_EIDAS"
    QES_ZERTES = "QES_ZERTES"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, EnvelopeLegalityLevel._member_map_.values()))
