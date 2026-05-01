from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..documents import DocumentsService
from ...net.sdk_config import SdkConfig


class DocumentsServiceAsync(DocumentsService):
    """
    Async Wrapper for DocumentsServiceAsync
    """

    def get_envelope_documents(
        self,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_envelope_documents)(
            envelope_id, accept, request_config=request_config
        )
