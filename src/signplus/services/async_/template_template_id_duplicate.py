from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id_duplicate import TemplateTemplateIdDuplicateService
from ...net.sdk_config import SdkConfig


class TemplateTemplateIdDuplicateServiceAsync(TemplateTemplateIdDuplicateService):
    """
    Async Wrapper for TemplateTemplateIdDuplicateServiceAsync
    """

    def duplicate_template(
        self,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().duplicate_template)(
            template_id, accept, request_config=request_config
        )
