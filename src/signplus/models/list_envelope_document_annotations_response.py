from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .annotation import Annotation


@JsonMap({})
class ListEnvelopeDocumentAnnotationsResponse(BaseModel):
    """ListEnvelopeDocumentAnnotationsResponse

    :param annotations: annotations, defaults to None
    :type annotations: List[Annotation], optional
    """

    def __init__(self, annotations: List[Annotation] = None):
        """ListEnvelopeDocumentAnnotationsResponse

        :param annotations: annotations, defaults to None
        :type annotations: List[Annotation], optional
        """
        if annotations is not None:
            self.annotations = self._define_list(annotations, Annotation)
