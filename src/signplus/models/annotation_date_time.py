from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .annotation_font import AnnotationFont
from .annotation_date_time_format import AnnotationDateTimeFormat


@JsonMap({})
class AnnotationDateTime(BaseModel):
    """Date annotation (null if annotation is not a date)

    :param size: Font size of the text in pt, defaults to None
    :type size: float, optional
    :param font: font, defaults to None
    :type font: AnnotationFont, optional
    :param color: Color of the text in hex format, defaults to None
    :type color: str, optional
    :param auto_fill: Whether the date should be automatically filled, defaults to None
    :type auto_fill: bool, optional
    :param timezone: Timezone of the date, defaults to None
    :type timezone: str, optional
    :param timestamp: Unix timestamp of the date, defaults to None
    :type timestamp: int, optional
    :param format: Format of the date time (DMY_NUMERIC_SLASH is day/month/year with slashes, MDY_NUMERIC_SLASH is month/day/year with slashes, YMD_NUMERIC_SLASH is year/month/day with slashes, DMY_NUMERIC_DASH_SHORT is day/month/year with dashes, DMY_NUMERIC_DASH is day/month/year with dashes, YMD_NUMERIC_DASH is year/month/day with dashes, MDY_TEXT_DASH_SHORT is month/day/year with dashes, MDY_TEXT_SPACE_SHORT is month/day/year with spaces, MDY_TEXT_SPACE is month/day/year with spaces), defaults to None
    :type format: AnnotationDateTimeFormat, optional
    """

    def __init__(
        self,
        size: float = None,
        font: AnnotationFont = None,
        color: str = None,
        auto_fill: bool = None,
        timezone: str = None,
        timestamp: int = None,
        format: AnnotationDateTimeFormat = None,
    ):
        """Date annotation (null if annotation is not a date)

        :param size: Font size of the text in pt, defaults to None
        :type size: float, optional
        :param font: font, defaults to None
        :type font: AnnotationFont, optional
        :param color: Color of the text in hex format, defaults to None
        :type color: str, optional
        :param auto_fill: Whether the date should be automatically filled, defaults to None
        :type auto_fill: bool, optional
        :param timezone: Timezone of the date, defaults to None
        :type timezone: str, optional
        :param timestamp: Unix timestamp of the date, defaults to None
        :type timestamp: int, optional
        :param format: Format of the date time (DMY_NUMERIC_SLASH is day/month/year with slashes, MDY_NUMERIC_SLASH is month/day/year with slashes, YMD_NUMERIC_SLASH is year/month/day with slashes, DMY_NUMERIC_DASH_SHORT is day/month/year with dashes, DMY_NUMERIC_DASH is day/month/year with dashes, YMD_NUMERIC_DASH is year/month/day with dashes, MDY_TEXT_DASH_SHORT is month/day/year with dashes, MDY_TEXT_SPACE_SHORT is month/day/year with spaces, MDY_TEXT_SPACE is month/day/year with spaces), defaults to None
        :type format: AnnotationDateTimeFormat, optional
        """
        if size is not None:
            self.size = size
        if font is not None:
            self.font = self._define_object(font, AnnotationFont)
        if color is not None:
            self.color = color
        if auto_fill is not None:
            self.auto_fill = auto_fill
        if timezone is not None:
            self.timezone = timezone
        if timestamp is not None:
            self.timestamp = timestamp
        if format is not None:
            self.format = self._enum_matching(
                format, AnnotationDateTimeFormat.list(), "format"
            )
