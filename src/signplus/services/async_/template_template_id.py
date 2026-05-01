from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id import TemplateTemplateIdService
from ...net.sdk_config import SdkConfig


class TemplateTemplateIdServiceAsync(TemplateTemplateIdService):
    """
    Async Wrapper for TemplateTemplateIdServiceAsync
    """

    def get_template(
        self,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_template)(
            template_id, accept, request_config=request_config
        )

    def delete_template(
        self, template_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:
        return to_async(super().delete_template)(
            template_id, request_config=request_config
        )
