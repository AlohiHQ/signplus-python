from enum import Enum


class EnvelopeOrderField(Enum):
    """An enumeration representing different categories.

    :cvar CREATION_DATE: "CREATION_DATE"
    :vartype CREATION_DATE: str
    :cvar MODIFICATION_DATE: "MODIFICATION_DATE"
    :vartype MODIFICATION_DATE: str
    :cvar NAME: "NAME"
    :vartype NAME: str
    :cvar STATUS: "STATUS"
    :vartype STATUS: str
    :cvar LAST_DOCUMENT_CHANGE: "LAST_DOCUMENT_CHANGE"
    :vartype LAST_DOCUMENT_CHANGE: str
    """

    CREATION_DATE = "CREATION_DATE"
    MODIFICATION_DATE = "MODIFICATION_DATE"
    NAME = "NAME"
    STATUS = "STATUS"
    LAST_DOCUMENT_CHANGE = "LAST_DOCUMENT_CHANGE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, EnvelopeOrderField._member_map_.values()))
