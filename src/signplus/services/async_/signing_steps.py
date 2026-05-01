from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..signing_steps import SigningStepsService
from ...net.sdk_config import SdkConfig
from ...models import AddEnvelopeSigningStepsRequest


class SigningStepsServiceAsync(SigningStepsService):
    """
    Async Wrapper for SigningStepsServiceAsync
    """

    def add_envelope_signing_steps(
        self,
        request_body: AddEnvelopeSigningStepsRequest,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().add_envelope_signing_steps)(
            request_body, envelope_id, accept, request_config=request_config
        )
