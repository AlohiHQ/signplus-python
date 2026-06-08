from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel
from .page import Page


class Document(BaseModel):
    """Document

    :param id_: Unique identifier of the document, defaults to None
    :type id_: str, optional
    :param name: Name of the document, defaults to None
    :type name: str, optional
    :param filename: Filename of the document, defaults to None
    :type filename: str, optional
    :param page_count: Number of pages in the document, defaults to None
    :type page_count: int, optional
    :param pages: List of pages in the document, defaults to None
    :type pages: List[Page], optional
    """

    id_: Optional[str] = Field(
        alias="id",
        serialization_alias="id",
        default=None,
        description="Unique identifier of the document",
    )
    name: Optional[str] = Field(default=None, description="Name of the document")
    filename: Optional[str] = Field(
        default=None, description="Filename of the document"
    )
    page_count: Optional[int] = Field(
        default=None, description="Number of pages in the document"
    )
    pages: Optional[List[Page]] = Field(
        default=None, description="List of pages in the document"
    )
