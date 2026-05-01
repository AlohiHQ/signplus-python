from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..envelope_id import EnvelopeIdService
from ...net.sdk_config import SdkConfig


class EnvelopeIdServiceAsync(EnvelopeIdService):
    """
    Async Wrapper for EnvelopeIdServiceAsync
    """

    def get_envelope(
        self,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_envelope)(
            envelope_id, accept, request_config=request_config
        )

    def delete_envelope(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:
        return to_async(super().delete_envelope)(
            envelope_id, request_config=request_config
        )
