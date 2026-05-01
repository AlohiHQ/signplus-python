from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id_documents import TemplateTemplateIdDocumentsService
from ...net.sdk_config import SdkConfig


class TemplateTemplateIdDocumentsServiceAsync(TemplateTemplateIdDocumentsService):
    """
    Async Wrapper for TemplateTemplateIdDocumentsServiceAsync
    """

    def get_template_documents(
        self,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_template_documents)(
            template_id, accept, request_config=request_config
        )
