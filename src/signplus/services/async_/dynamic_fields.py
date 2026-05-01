from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..dynamic_fields import DynamicFieldsService
from ...net.sdk_config import SdkConfig
from ...models import SetEnvelopeDynamicFieldsRequest


class DynamicFieldsServiceAsync(DynamicFieldsService):
    """
    Async Wrapper for DynamicFieldsServiceAsync
    """

    def set_envelope_dynamic_fields(
        self,
        request_body: SetEnvelopeDynamicFieldsRequest,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().set_envelope_dynamic_fields)(
            request_body, envelope_id, accept, request_config=request_config
        )
