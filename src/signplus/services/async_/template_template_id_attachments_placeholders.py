from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id_attachments_placeholders import (
    TemplateTemplateIdAttachmentsPlaceholdersService,
)
from ...net.sdk_config import SdkConfig
from ...models import SetTemplateAttachmentsPlaceholdersRequest


class TemplateTemplateIdAttachmentsPlaceholdersServiceAsync(
    TemplateTemplateIdAttachmentsPlaceholdersService
):
    """
    Async Wrapper for TemplateTemplateIdAttachmentsPlaceholdersServiceAsync
    """

    def set_template_attachments_placeholders(
        self,
        request_body: SetTemplateAttachmentsPlaceholdersRequest,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().set_template_attachments_placeholders)(
            request_body, template_id, accept, request_config=request_config
        )
