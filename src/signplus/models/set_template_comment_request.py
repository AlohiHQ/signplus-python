from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class SetTemplateCommentRequest(BaseModel):
    """SetTemplateCommentRequest

    :param comment: Comment for the template, defaults to None
    :type comment: str, optional
    """

    def __init__(self, comment: str = None):
        """SetTemplateCommentRequest

        :param comment: Comment for the template, defaults to None
        :type comment: str, optional
        """
        if comment is not None:
            self.comment = comment
