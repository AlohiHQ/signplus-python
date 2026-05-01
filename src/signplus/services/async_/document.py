from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..document import DocumentService
from ...net.sdk_config import SdkConfig
from ...models import AddEnvelopeDocumentRequest


class DocumentServiceAsync(DocumentService):
    """
    Async Wrapper for DocumentServiceAsync
    """

    def add_envelope_document(
        self,
        request_body: AddEnvelopeDocumentRequest,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().add_envelope_document)(
            request_body, envelope_id, accept, request_config=request_config
        )
