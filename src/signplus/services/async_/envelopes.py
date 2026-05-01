from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..envelopes import EnvelopesService
from ...net.sdk_config import SdkConfig
from ...models import ListEnvelopesRequest


class EnvelopesServiceAsync(EnvelopesService):
    """
    Async Wrapper for EnvelopesServiceAsync
    """

    def list_envelopes(
        self,
        request_body: ListEnvelopesRequest,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().list_envelopes)(
            request_body, accept, request_config=request_config
        )
