from enum import Enum


class EnvelopeFlowType(Enum):
    """An enumeration representing different categories.

    :cvar REQUESTSIGNATURE: "REQUEST_SIGNATURE"
    :vartype REQUESTSIGNATURE: str
    """

    REQUESTSIGNATURE = "REQUEST_SIGNATURE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, EnvelopeFlowType._member_map_.values()))
