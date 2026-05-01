from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id_document import TemplateTemplateIdDocumentService
from ...net.sdk_config import SdkConfig
from ...models import AddTemplateDocumentRequest


class TemplateTemplateIdDocumentServiceAsync(TemplateTemplateIdDocumentService):
    """
    Async Wrapper for TemplateTemplateIdDocumentServiceAsync
    """

    def add_template_document(
        self,
        request_body: AddTemplateDocumentRequest,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().add_template_document)(
            request_body, template_id, accept, request_config=request_config
        )
