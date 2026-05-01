from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..envelope import EnvelopeService
from ...net.sdk_config import SdkConfig
from ...models import CreateEnvelopeRequest


class EnvelopeServiceAsync(EnvelopeService):
    """
    Async Wrapper for EnvelopeServiceAsync
    """

    def create_envelope(
        self,
        request_body: CreateEnvelopeRequest,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().create_envelope)(
            request_body, accept, request_config=request_config
        )
