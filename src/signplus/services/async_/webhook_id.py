from typing import Awaitable, Optional, Any
from .utils.to_async import to_async
from ..webhook_id import WebhookIdService
from ...net.sdk_config import SdkConfig


class WebhookIdServiceAsync(WebhookIdService):
    """
    Async Wrapper for WebhookIdServiceAsync
    """

    def delete_webhook(
        self, webhook_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:
        return to_async(super().delete_webhook)(
            webhook_id, request_config=request_config
        )
