from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..envelope_envelope_id_annotations_document_id import (
    EnvelopeEnvelopeIdAnnotationsDocumentIdService,
)
from ...net.sdk_config import SdkConfig


class EnvelopeEnvelopeIdAnnotationsDocumentIdServiceAsync(
    EnvelopeEnvelopeIdAnnotationsDocumentIdService
):
    """
    Async Wrapper for EnvelopeEnvelopeIdAnnotationsDocumentIdServiceAsync
    """

    def get_envelope_document_annotations(
        self,
        envelope_id: str,
        document_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_envelope_document_annotations)(
            envelope_id, document_id, accept, request_config=request_config
        )
