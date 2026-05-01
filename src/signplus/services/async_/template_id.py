from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_id import TemplateIdService
from ...net.sdk_config import SdkConfig
from ...models import CreateEnvelopeFromTemplateRequest


class TemplateIdServiceAsync(TemplateIdService):
    """
    Async Wrapper for TemplateIdServiceAsync
    """

    def create_envelope_from_template(
        self,
        request_body: CreateEnvelopeFromTemplateRequest,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().create_envelope_from_template)(
            request_body, template_id, accept, request_config=request_config
        )
