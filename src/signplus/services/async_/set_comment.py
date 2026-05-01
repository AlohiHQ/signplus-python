from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..set_comment import SetCommentService
from ...net.sdk_config import SdkConfig
from ...models import SetEnvelopeCommentRequest


class SetCommentServiceAsync(SetCommentService):
    """
    Async Wrapper for SetCommentServiceAsync
    """

    def set_envelope_comment(
        self,
        request_body: SetEnvelopeCommentRequest,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().set_envelope_comment)(
            request_body, envelope_id, accept, request_config=request_config
        )
