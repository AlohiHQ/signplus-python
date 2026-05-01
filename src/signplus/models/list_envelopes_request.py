from typing import List
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class ListEnvelopesRequest(BaseModel):
    """ListEnvelopesRequest

    :param name: name, defaults to None
    :type name: str, optional
    :param tags: tags, defaults to None
    :type tags: List[str], optional
    :param comment: comment, defaults to None
    :type comment: str, optional
    :param ids: ids, defaults to None
    :type ids: List[str], optional
    :param statuses: statuses, defaults to None
    :type statuses: List[str], optional
    :param folder_ids: folder_ids, defaults to None
    :type folder_ids: List[str], optional
    :param only_root_folder: only_root_folder, defaults to None
    :type only_root_folder: str, optional
    :param date_from: date_from, defaults to None
    :type date_from: str, optional
    :param date_to: date_to, defaults to None
    :type date_to: str, optional
    :param uid: uid, defaults to None
    :type uid: str, optional
    :param first: first, defaults to None
    :type first: str, optional
    :param last: last, defaults to None
    :type last: str, optional
    :param after: after, defaults to None
    :type after: str, optional
    :param before: before, defaults to None
    :type before: str, optional
    :param order_field: order_field, defaults to None
    :type order_field: str, optional
    :param ascending: ascending, defaults to None
    :type ascending: str, optional
    :param include_trash: include_trash, defaults to None
    :type include_trash: str, optional
    """

    name: Optional[str] = Field(default=None)
    tags: Optional[List[str]] = Field(default=None)
    comment: Optional[str] = Field(default=None)
    ids: Optional[List[str]] = Field(default=None)
    statuses: Optional[List[str]] = Field(default=None)
    folder_ids: Optional[List[str]] = Field(default=None)
    only_root_folder: Optional[str] = Field(default=None)
    date_from: Optional[str] = Field(default=None)
    date_to: Optional[str] = Field(default=None)
    uid: Optional[str] = Field(default=None)
    first: Optional[str] = Field(default=None)
    last: Optional[str] = Field(default=None)
    after: Optional[str] = Field(default=None)
    before: Optional[str] = Field(default=None)
    order_field: Optional[str] = Field(default=None)
    ascending: Optional[str] = Field(default=None)
    include_trash: Optional[str] = Field(default=None)
