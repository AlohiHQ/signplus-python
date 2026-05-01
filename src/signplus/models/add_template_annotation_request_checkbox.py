from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class AddTemplateAnnotationRequestCheckbox(BaseModel):
    """AddTemplateAnnotationRequestCheckbox

    :param checked: checked, defaults to None
    :type checked: str, optional
    :param style: style, defaults to None
    :type style: str, optional
    """

    checked: Optional[str] = Field(default=None)
    style: Optional[str] = Field(default=None)
