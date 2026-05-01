from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..annotation import AnnotationService
from ...net.sdk_config import SdkConfig
from ...models import AddEnvelopeAnnotationRequest


class AnnotationServiceAsync(AnnotationService):
    """
    Async Wrapper for AnnotationServiceAsync
    """

    def add_envelope_annotation(
        self,
        request_body: AddEnvelopeAnnotationRequest,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().add_envelope_annotation)(
            request_body, envelope_id, accept, request_config=request_config
        )
