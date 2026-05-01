from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..signed_documents import SignedDocumentsService
from ...net.sdk_config import SdkConfig
from ...models.utils.sentinel import SENTINEL


class SignedDocumentsServiceAsync(SignedDocumentsService):
    """
    Async Wrapper for SignedDocumentsServiceAsync
    """

    def download_envelope_signed_documents(
        self,
        envelope_id: str,
        accept: Union[str, None],
        certificate_of_completion: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().download_envelope_signed_documents)(
            envelope_id,
            accept,
            certificate_of_completion,
            request_config=request_config,
        )
