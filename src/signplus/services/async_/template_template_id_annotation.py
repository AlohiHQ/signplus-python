from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id_annotation import TemplateTemplateIdAnnotationService
from ...net.sdk_config import SdkConfig
from ...models import AddTemplateAnnotationRequest


class TemplateTemplateIdAnnotationServiceAsync(TemplateTemplateIdAnnotationService):
    """
    Async Wrapper for TemplateTemplateIdAnnotationServiceAsync
    """

    def add_template_annotation(
        self,
        request_body: AddTemplateAnnotationRequest,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().add_template_annotation)(
            request_body, template_id, accept, request_config=request_config
        )
