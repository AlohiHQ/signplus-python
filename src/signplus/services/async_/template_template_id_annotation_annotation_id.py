from typing import Awaitable, Optional, Any
from .utils.to_async import to_async
from ..template_template_id_annotation_annotation_id import (
    TemplateTemplateIdAnnotationAnnotationIdService,
)
from ...net.sdk_config import SdkConfig


class TemplateTemplateIdAnnotationAnnotationIdServiceAsync(
    TemplateTemplateIdAnnotationAnnotationIdService
):
    """
    Async Wrapper for TemplateTemplateIdAnnotationAnnotationIdServiceAsync
    """

    def delete_template_annotation(
        self,
        template_id: str,
        annotation_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().delete_template_annotation)(
            template_id, annotation_id, request_config=request_config
        )
