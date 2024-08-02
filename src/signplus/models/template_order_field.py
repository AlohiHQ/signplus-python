from enum import Enum


class TemplateOrderField(Enum):
    """An enumeration representing different categories.

    :cvar TEMPLATE_ID: "TEMPLATE_ID"
    :vartype TEMPLATE_ID: str
    :cvar TEMPLATE_CREATION_DATE: "TEMPLATE_CREATION_DATE"
    :vartype TEMPLATE_CREATION_DATE: str
    :cvar TEMPLATE_MODIFICATION_DATE: "TEMPLATE_MODIFICATION_DATE"
    :vartype TEMPLATE_MODIFICATION_DATE: str
    :cvar TEMPLATE_NAME: "TEMPLATE_NAME"
    :vartype TEMPLATE_NAME: str
    """

    TEMPLATE_ID = "TEMPLATE_ID"
    TEMPLATE_CREATION_DATE = "TEMPLATE_CREATION_DATE"
    TEMPLATE_MODIFICATION_DATE = "TEMPLATE_MODIFICATION_DATE"
    TEMPLATE_NAME = "TEMPLATE_NAME"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, TemplateOrderField._member_map_.values()))
