from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id_set_notification import (
    TemplateTemplateIdSetNotificationService,
)
from ...net.sdk_config import SdkConfig
from ...models import SetTemplateNotificationRequest


class TemplateTemplateIdSetNotificationServiceAsync(
    TemplateTemplateIdSetNotificationService
):
    """
    Async Wrapper for TemplateTemplateIdSetNotificationServiceAsync
    """

    def set_template_notification(
        self,
        request_body: SetTemplateNotificationRequest,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().set_template_notification)(
            request_body, template_id, accept, request_config=request_config
        )
