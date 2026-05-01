from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..set_expiration_date import SetExpirationDateService
from ...net.sdk_config import SdkConfig
from ...models import SetEnvelopeExpirationDateRequest


class SetExpirationDateServiceAsync(SetExpirationDateService):
    """
    Async Wrapper for SetExpirationDateServiceAsync
    """

    def set_envelope_expiration_date(
        self,
        request_body: SetEnvelopeExpirationDateRequest,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().set_envelope_expiration_date)(
            request_body, envelope_id, accept, request_config=request_config
        )
