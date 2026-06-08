from enum import Enum


class RecipientRole(str, Enum):
    """An enumeration representing different categories.

    :cvar SIGNER: "SIGNER"
    :vartype SIGNER: str
    :cvar RECEIVESCOPY: "RECEIVES_COPY"
    :vartype RECEIVESCOPY: str
    :cvar INPERSONSIGNER: "IN_PERSON_SIGNER"
    :vartype INPERSONSIGNER: str
    """

    SIGNER = "SIGNER"
    RECEIVESCOPY = "RECEIVES_COPY"
    INPERSONSIGNER = "IN_PERSON_SIGNER"

    @staticmethod
    def list():
        """Lists all enum values.

        :return: A list of all enum values.
        :rtype: list
        """
        return list(map(lambda x: x.value, RecipientRole._member_map_.values()))
