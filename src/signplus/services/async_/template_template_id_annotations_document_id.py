from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id_annotations_document_id import (
    TemplateTemplateIdAnnotationsDocumentIdService,
)
from ...net.sdk_config import SdkConfig


class TemplateTemplateIdAnnotationsDocumentIdServiceAsync(
    TemplateTemplateIdAnnotationsDocumentIdService
):
    """
    Async Wrapper for TemplateTemplateIdAnnotationsDocumentIdServiceAsync
    """

    def get_document_template_annotations(
        self,
        template_id: str,
        document_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_document_template_annotations)(
            template_id, document_id, accept, request_config=request_config
        )
