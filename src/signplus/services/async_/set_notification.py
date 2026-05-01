from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..set_notification import SetNotificationService
from ...net.sdk_config import SdkConfig
from ...models import SetEnvelopeNotificationRequest


class SetNotificationServiceAsync(SetNotificationService):
    """
    Async Wrapper for SetNotificationServiceAsync
    """

    def set_envelope_notification(
        self,
        request_body: SetEnvelopeNotificationRequest,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().set_envelope_notification)(
            request_body, envelope_id, accept, request_config=request_config
        )
