from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..send import SendService
from ...net.sdk_config import SdkConfig


class SendServiceAsync(SendService):
    """
    Async Wrapper for SendServiceAsync
    """

    def send_envelope(
        self,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().send_envelope)(
            envelope_id, accept, request_config=request_config
        )
