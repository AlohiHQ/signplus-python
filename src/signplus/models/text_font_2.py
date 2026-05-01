from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class TextFont2(BaseModel):
    """TextFont2

    :param family: family, defaults to None
    :type family: str, optional
    :param italic: italic, defaults to None
    :type italic: str, optional
    :param bold: bold, defaults to None
    :type bold: str, optional
    """

    family: Optional[str] = Field(default=None)
    italic: Optional[str] = Field(default=None)
    bold: Optional[str] = Field(default=None)
