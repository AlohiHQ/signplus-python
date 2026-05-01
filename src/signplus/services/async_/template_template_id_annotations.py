from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id_annotations import TemplateTemplateIdAnnotationsService
from ...net.sdk_config import SdkConfig


class TemplateTemplateIdAnnotationsServiceAsync(TemplateTemplateIdAnnotationsService):
    """
    Async Wrapper for TemplateTemplateIdAnnotationsServiceAsync
    """

    def get_template_annotations(
        self,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_template_annotations)(
            template_id, accept, request_config=request_config
        )
