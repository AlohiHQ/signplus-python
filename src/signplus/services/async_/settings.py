from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..settings import SettingsService
from ...net.sdk_config import SdkConfig
from ...models import SetEnvelopeAttachmentsSettingsRequest


class SettingsServiceAsync(SettingsService):
    """
    Async Wrapper for SettingsServiceAsync
    """

    def set_envelope_attachments_settings(
        self,
        request_body: SetEnvelopeAttachmentsSettingsRequest,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().set_envelope_attachments_settings)(
            request_body, envelope_id, accept, request_config=request_config
        )
