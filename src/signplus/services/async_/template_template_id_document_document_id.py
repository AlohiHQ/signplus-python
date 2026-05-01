from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id_document_document_id import (
    TemplateTemplateIdDocumentDocumentIdService,
)
from ...net.sdk_config import SdkConfig


class TemplateTemplateIdDocumentDocumentIdServiceAsync(
    TemplateTemplateIdDocumentDocumentIdService
):
    """
    Async Wrapper for TemplateTemplateIdDocumentDocumentIdServiceAsync
    """

    def get_template_document(
        self,
        template_id: str,
        document_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_template_document)(
            template_id, document_id, accept, request_config=request_config
        )
