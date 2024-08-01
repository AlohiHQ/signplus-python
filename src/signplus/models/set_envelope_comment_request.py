from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class SetEnvelopeCommentRequest(BaseModel):
    """SetEnvelopeCommentRequest

    :param comment: Comment for the envelope, defaults to None
    :type comment: str, optional
    """

    def __init__(self, comment: str = None):
        """SetEnvelopeCommentRequest

        :param comment: Comment for the envelope, defaults to None
        :type comment: str, optional
        """
        if comment is not None:
            self.comment = comment
