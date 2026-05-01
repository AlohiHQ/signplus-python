from __future__ import annotations
from typing import List
from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel
from .set_template_attachments_placeholders_request_placeholders import (
    SetTemplateAttachmentsPlaceholdersRequestPlaceholders,
)


class SetTemplateAttachmentsPlaceholdersRequest(BaseModel):
    """SetTemplateAttachmentsPlaceholdersRequest

    :param placeholders: placeholders, defaults to None
    :type placeholders: List[SetTemplateAttachmentsPlaceholdersRequestPlaceholders], optional
    """

    placeholders: Optional[
        List[SetTemplateAttachmentsPlaceholdersRequestPlaceholders]
    ] = Field(default=None)
