from typing import Awaitable, Optional, Any
from .utils.to_async import to_async
from ..annotation_id import AnnotationIdService
from ...net.sdk_config import SdkConfig


class AnnotationIdServiceAsync(AnnotationIdService):
    """
    Async Wrapper for AnnotationIdServiceAsync
    """

    def delete_envelope_annotation(
        self,
        envelope_id: str,
        annotation_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().delete_envelope_annotation)(
            envelope_id, annotation_id, request_config=request_config
        )
