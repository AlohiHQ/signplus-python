from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..placeholders import PlaceholdersService
from ...net.sdk_config import SdkConfig
from ...models import SetEnvelopeAttachmentsPlaceholdersRequest


class PlaceholdersServiceAsync(PlaceholdersService):
    """
    Async Wrapper for PlaceholdersServiceAsync
    """

    def set_envelope_attachments_placeholders(
        self,
        request_body: SetEnvelopeAttachmentsPlaceholdersRequest,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().set_envelope_attachments_placeholders)(
            request_body, envelope_id, accept, request_config=request_config
        )
