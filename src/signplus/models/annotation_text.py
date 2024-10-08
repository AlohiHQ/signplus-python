from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .annotation_font import AnnotationFont


@JsonMap({})
class AnnotationText(BaseModel):
    """Text annotation (null if annotation is not a text)

    :param size: Font size of the text in pt, defaults to None
    :type size: float, optional
    :param color: Text color in 32bit representation, defaults to None
    :type color: float, optional
    :param value: Text content of the annotation, defaults to None
    :type value: str, optional
    :param tooltip: Tooltip of the annotation, defaults to None
    :type tooltip: str, optional
    :param dynamic_field_name: Name of the dynamic field, defaults to None
    :type dynamic_field_name: str, optional
    :param font: font, defaults to None
    :type font: AnnotationFont, optional
    """

    def __init__(
        self,
        size: float = None,
        color: float = None,
        value: str = None,
        tooltip: str = None,
        dynamic_field_name: str = None,
        font: AnnotationFont = None,
    ):
        """Text annotation (null if annotation is not a text)

        :param size: Font size of the text in pt, defaults to None
        :type size: float, optional
        :param color: Text color in 32bit representation, defaults to None
        :type color: float, optional
        :param value: Text content of the annotation, defaults to None
        :type value: str, optional
        :param tooltip: Tooltip of the annotation, defaults to None
        :type tooltip: str, optional
        :param dynamic_field_name: Name of the dynamic field, defaults to None
        :type dynamic_field_name: str, optional
        :param font: font, defaults to None
        :type font: AnnotationFont, optional
        """
        if size is not None:
            self.size = size
        if color is not None:
            self.color = color
        if value is not None:
            self.value = value
        if tooltip is not None:
            self.tooltip = tooltip
        if dynamic_field_name is not None:
            self.dynamic_field_name = dynamic_field_name
        if font is not None:
            self.font = self._define_object(font, AnnotationFont)
