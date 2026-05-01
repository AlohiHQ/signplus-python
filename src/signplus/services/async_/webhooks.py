from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..webhooks import WebhooksService
from ...net.sdk_config import SdkConfig
from ...models import ListWebhooksRequest


class WebhooksServiceAsync(WebhooksService):
    """
    Async Wrapper for WebhooksServiceAsync
    """

    def list_webhooks(
        self,
        request_body: ListWebhooksRequest,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().list_webhooks)(
            request_body, accept, request_config=request_config
        )
