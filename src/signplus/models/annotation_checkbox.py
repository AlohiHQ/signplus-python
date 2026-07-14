from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .annotation_checkbox_style import AnnotationCheckboxStyle


class AnnotationCheckbox(BaseModel):
    """Checkbox annotation (null if annotation is not a checkbox)

    :param checked: Whether the checkbox is checked, defaults to None
    :type checked: bool, optional
    :param style: Style of the checkbox, defaults to None
    :type style: AnnotationCheckboxStyle, optional
    """

    checked: Optional[bool] = Field(
        default=None, description="Whether the checkbox is checked"
    )
    style: Optional[AnnotationCheckboxStyle] = Field(
        default=None, description="Style of the checkbox"
    )
