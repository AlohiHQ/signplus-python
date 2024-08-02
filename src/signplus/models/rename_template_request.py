from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class RenameTemplateRequest(BaseModel):
    """RenameTemplateRequest

    :param name: Name of the template, defaults to None
    :type name: str, optional
    """

    def __init__(self, name: str = None):
        """RenameTemplateRequest

        :param name: Name of the template, defaults to None
        :type name: str, optional
        """
        if name is not None:
            self.name = name
