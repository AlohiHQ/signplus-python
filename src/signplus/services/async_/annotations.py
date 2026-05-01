from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..annotations import AnnotationsService
from ...net.sdk_config import SdkConfig


class AnnotationsServiceAsync(AnnotationsService):
    """
    Async Wrapper for AnnotationsServiceAsync
    """

    def get_envelope_annotations(
        self,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_envelope_annotations)(
            envelope_id, accept, request_config=request_config
        )
