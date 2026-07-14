from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .document import Document


class ListTemplateDocumentsResponse(BaseModel):
    """ListTemplateDocumentsResponse

    :param documents: documents, defaults to None
    :type documents: List[Document], optional
    """

    documents: Optional[List[Document]] = Field(default=None)
