from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id_attachments_settings import (
    TemplateTemplateIdAttachmentsSettingsService,
)
from ...net.sdk_config import SdkConfig
from ...models import SetTemplateAttachmentsSettingsRequest


class TemplateTemplateIdAttachmentsSettingsServiceAsync(
    TemplateTemplateIdAttachmentsSettingsService
):
    """
    Async Wrapper for TemplateTemplateIdAttachmentsSettingsServiceAsync
    """

    def set_template_attachments_settings(
        self,
        request_body: SetTemplateAttachmentsSettingsRequest,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().set_template_attachments_settings)(
            request_body, template_id, accept, request_config=request_config
        )
