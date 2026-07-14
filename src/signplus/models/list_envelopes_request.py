from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .envelope_status import EnvelopeStatus
from .envelope_order_field import EnvelopeOrderField


class ListEnvelopesRequest(BaseModel):
    """ListEnvelopesRequest

    :param name: Name of the envelope, defaults to None
    :type name: str, optional
    :param tags: List of tags, defaults to None
    :type tags: List[str], optional
    :param comment: Comment of the envelope, defaults to None
    :type comment: str, optional
    :param ids: List of envelope IDs, defaults to None
    :type ids: List[str], optional
    :param statuses: List of envelope statuses, defaults to None
    :type statuses: List[EnvelopeStatus], optional
    :param folder_ids: List of folder IDs, defaults to None
    :type folder_ids: List[str], optional
    :param only_root_folder: Whether to only list envelopes in the root folder, defaults to None
    :type only_root_folder: bool, optional
    :param date_from: Unix timestamp of the start date, defaults to None
    :type date_from: int, optional
    :param date_to: Unix timestamp of the end date, defaults to None
    :type date_to: int, optional
    :param uid: Unique identifier of the user, defaults to None
    :type uid: str, optional
    :param first: first, defaults to None
    :type first: int, optional
    :param last: last, defaults to None
    :type last: int, optional
    :param after: after, defaults to None
    :type after: str, optional
    :param before: before, defaults to None
    :type before: str, optional
    :param order_field: Field to order envelopes by, defaults to None
    :type order_field: EnvelopeOrderField, optional
    :param ascending: Whether to order envelopes in ascending order, defaults to None
    :type ascending: bool, optional
    :param include_trash: Whether to include envelopes in the trash, defaults to None
    :type include_trash: bool, optional
    """

    name: Optional[str] = Field(default=None, description="Name of the envelope")
    tags: Optional[List[str]] = Field(default=None, description="List of tags")
    comment: Optional[str] = Field(default=None, description="Comment of the envelope")
    ids: Optional[List[str]] = Field(default=None, description="List of envelope IDs")
    statuses: Optional[List[EnvelopeStatus]] = Field(
        default=None, description="List of envelope statuses"
    )
    folder_ids: Optional[List[str]] = Field(
        default=None, description="List of folder IDs"
    )
    only_root_folder: Optional[bool] = Field(
        default=None, description="Whether to only list envelopes in the root folder"
    )
    date_from: Optional[int] = Field(
        default=None, description="Unix timestamp of the start date"
    )
    date_to: Optional[int] = Field(
        default=None, description="Unix timestamp of the end date"
    )
    uid: Optional[str] = Field(
        default=None, description="Unique identifier of the user"
    )
    first: Optional[int] = Field(default=None)
    last: Optional[int] = Field(default=None)
    after: Optional[str] = Field(default=None)
    before: Optional[str] = Field(default=None)
    order_field: Optional[EnvelopeOrderField] = Field(
        default=None, description="Field to order envelopes by"
    )
    ascending: Optional[bool] = Field(
        default=None, description="Whether to order envelopes in ascending order"
    )
    include_trash: Optional[bool] = Field(
        default=None, description="Whether to include envelopes in the trash"
    )
