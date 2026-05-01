from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..document_id import DocumentIdService
from ...net.sdk_config import SdkConfig


class DocumentIdServiceAsync(DocumentIdService):
    """
    Async Wrapper for DocumentIdServiceAsync
    """

    def get_envelope_document(
        self,
        envelope_id: str,
        document_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_envelope_document)(
            envelope_id, document_id, accept, request_config=request_config
        )
