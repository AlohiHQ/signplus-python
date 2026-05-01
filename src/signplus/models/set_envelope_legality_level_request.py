from pydantic import Field
from typing import Optional
from typing import Union
from .utils.base_model import BaseModel


class SetEnvelopeLegalityLevelRequest(BaseModel):
    """SetEnvelopeLegalityLevelRequest

    :param legality_level: legality_level, defaults to None
    :type legality_level: str, optional
    """

    legality_level: Optional[str] = Field(default=None)
