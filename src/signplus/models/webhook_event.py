from enum import Enum


class WebhookEvent(Enum):
    """An enumeration representing different categories.

    :cvar ENVELOPE_EXPIRED: "ENVELOPE_EXPIRED"
    :vartype ENVELOPE_EXPIRED: str
    :cvar ENVELOPE_DECLINED: "ENVELOPE_DECLINED"
    :vartype ENVELOPE_DECLINED: str
    :cvar ENVELOPE_VOIDED: "ENVELOPE_VOIDED"
    :vartype ENVELOPE_VOIDED: str
    :cvar ENVELOPE_COMPLETED: "ENVELOPE_COMPLETED"
    :vartype ENVELOPE_COMPLETED: str
    """

    ENVELOPE_EXPIRED = "ENVELOPE_EXPIRED"
    ENVELOPE_DECLINED = "ENVELOPE_DECLINED"
    ENVELOPE_VOIDED = "ENVELOPE_VOIDED"
    ENVELOPE_COMPLETED = "ENVELOPE_COMPLETED"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, WebhookEvent._member_map_.values()))
