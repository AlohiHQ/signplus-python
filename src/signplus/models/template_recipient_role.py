from enum import Enum


class TemplateRecipientRole(Enum):
    """An enumeration representing different categories.

    :cvar SIGNER: "SIGNER"
    :vartype SIGNER: str
    :cvar RECEIVES_COPY: "RECEIVES_COPY"
    :vartype RECEIVES_COPY: str
    :cvar IN_PERSON_SIGNER: "IN_PERSON_SIGNER"
    :vartype IN_PERSON_SIGNER: str
    """

    SIGNER = "SIGNER"
    RECEIVES_COPY = "RECEIVES_COPY"
    IN_PERSON_SIGNER = "IN_PERSON_SIGNER"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, TemplateRecipientRole._member_map_.values()))
