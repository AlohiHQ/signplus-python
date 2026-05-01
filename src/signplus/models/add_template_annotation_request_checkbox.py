from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class AddTemplateAnnotationRequestCheckbox(BaseModel):
    """AddTemplateAnnotationRequestCheckbox

    :param checked: checked, defaults to None
    :type checked: bool, optional
    :param style: style, defaults to None
    :type style: str, optional
    """

    checked: Optional[bool] = Field(default=None)
    style: Optional[str] = Field(default=None)
