from enum import Enum


class EnvelopeFlowType(Enum):
    """An enumeration representing different categories.

    :cvar REQUEST_SIGNATURE: "REQUEST_SIGNATURE"
    :vartype REQUEST_SIGNATURE: str
    :cvar SIGN_MYSELF: "SIGN_MYSELF"
    :vartype SIGN_MYSELF: str
    """

    REQUEST_SIGNATURE = "REQUEST_SIGNATURE"
    SIGN_MYSELF = "SIGN_MYSELF"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, EnvelopeFlowType._member_map_.values()))
