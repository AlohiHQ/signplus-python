from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template import TemplateService
from ...net.sdk_config import SdkConfig
from ...models import CreateTemplateRequest


class TemplateServiceAsync(TemplateService):
    """
    Async Wrapper for TemplateServiceAsync
    """

    def create_template(
        self,
        request_body: CreateTemplateRequest,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().create_template)(
            request_body, accept, request_config=request_config
        )
