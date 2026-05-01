from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..rename import RenameService
from ...net.sdk_config import SdkConfig
from ...models import RenameEnvelopeRequest


class RenameServiceAsync(RenameService):
    """
    Async Wrapper for RenameServiceAsync
    """

    def rename_envelope(
        self,
        request_body: RenameEnvelopeRequest,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().rename_envelope)(
            request_body, envelope_id, accept, request_config=request_config
        )
