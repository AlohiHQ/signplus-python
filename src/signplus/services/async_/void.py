from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..void import VoidService
from ...net.sdk_config import SdkConfig


class VoidServiceAsync(VoidService):
    """
    Async Wrapper for VoidServiceAsync
    """

    def void_envelope(
        self,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().void_envelope)(
            envelope_id, accept, request_config=request_config
        )
