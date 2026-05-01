from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..set_legality_level import SetLegalityLevelService
from ...net.sdk_config import SdkConfig
from ...models import SetEnvelopeLegalityLevelRequest


class SetLegalityLevelServiceAsync(SetLegalityLevelService):
    """
    Async Wrapper for SetLegalityLevelServiceAsync
    """

    def set_envelope_legality_level(
        self,
        request_body: SetEnvelopeLegalityLevelRequest,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().set_envelope_legality_level)(
            request_body, envelope_id, accept, request_config=request_config
        )
