from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .annotation_font_family import AnnotationFontFamily


@JsonMap({})
class AnnotationFont(BaseModel):
    """AnnotationFont

    :param family: Font family of the text, defaults to None
    :type family: AnnotationFontFamily, optional
    :param italic: Whether the text is italic, defaults to None
    :type italic: bool, optional
    :param bold: Whether the text is bold, defaults to None
    :type bold: bool, optional
    """

    def __init__(
        self,
        family: AnnotationFontFamily = None,
        italic: bool = None,
        bold: bool = None,
    ):
        """AnnotationFont

        :param family: Font family of the text, defaults to None
        :type family: AnnotationFontFamily, optional
        :param italic: Whether the text is italic, defaults to None
        :type italic: bool, optional
        :param bold: Whether the text is bold, defaults to None
        :type bold: bool, optional
        """
        if family is not None:
            self.family = self._enum_matching(
                family, AnnotationFontFamily.list(), "family"
            )
        if italic is not None:
            self.italic = italic
        if bold is not None:
            self.bold = bold
