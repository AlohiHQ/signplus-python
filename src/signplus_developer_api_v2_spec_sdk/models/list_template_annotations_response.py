from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel
from .annotation import Annotation


class ListTemplateAnnotationsResponse(BaseModel):
    """ListTemplateAnnotationsResponse

    :param annotations: annotations, defaults to None
    :type annotations: List[Annotation], optional
    """

    annotations: Optional[List[Annotation]] = Field(default=None)
