from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..templates import TemplatesService
from ...net.sdk_config import SdkConfig
from ...models import ListTemplatesRequest


class TemplatesServiceAsync(TemplatesService):
    """
    Async Wrapper for TemplatesServiceAsync
    """

    def list_templates(
        self,
        request_body: ListTemplatesRequest,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().list_templates)(
            request_body, accept, request_config=request_config
        )
