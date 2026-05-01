from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..duplicate import DuplicateService
from ...net.sdk_config import SdkConfig


class DuplicateServiceAsync(DuplicateService):
    """
    Async Wrapper for DuplicateServiceAsync
    """

    def duplicate_envelope(
        self,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().duplicate_envelope)(
            envelope_id, accept, request_config=request_config
        )
