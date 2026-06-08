from enum import Enum


class EnvelopeFlowType(str, Enum):
    """An enumeration representing different categories.

    :cvar REQUESTSIGNATURE: "REQUEST_SIGNATURE"
    :vartype REQUESTSIGNATURE: str
    :cvar SIGNMYSELF: "SIGN_MYSELF"
    :vartype SIGNMYSELF: str
    """

    REQUESTSIGNATURE = "REQUEST_SIGNATURE"
    SIGNMYSELF = "SIGN_MYSELF"

    @staticmethod
    def list():
        """Lists all enum values.

        :return: A list of all enum values.
        :rtype: list
        """
        return list(map(lambda x: x.value, EnvelopeFlowType._member_map_.values()))
