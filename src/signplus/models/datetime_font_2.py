from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class DatetimeFont2(BaseModel):
    """DatetimeFont2

    :param family: family, defaults to None
    :type family: str, optional
    :param italic: italic, defaults to None
    :type italic: bool, optional
    :param bold: bold, defaults to None
    :type bold: bool, optional
    """

    family: Optional[str] = Field(default=None)
    italic: Optional[bool] = Field(default=None)
    bold: Optional[bool] = Field(default=None)
