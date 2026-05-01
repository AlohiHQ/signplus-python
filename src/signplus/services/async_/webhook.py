from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..webhook import WebhookService
from ...net.sdk_config import SdkConfig
from ...models import CreateWebhookRequest


class WebhookServiceAsync(WebhookService):
    """
    Async Wrapper for WebhookServiceAsync
    """

    def create_webhook(
        self,
        request_body: CreateWebhookRequest,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().create_webhook)(
            request_body, accept, request_config=request_config
        )
