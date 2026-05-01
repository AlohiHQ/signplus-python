from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id_set_comment import TemplateTemplateIdSetCommentService
from ...net.sdk_config import SdkConfig
from ...models import SetTemplateCommentRequest


class TemplateTemplateIdSetCommentServiceAsync(TemplateTemplateIdSetCommentService):
    """
    Async Wrapper for TemplateTemplateIdSetCommentServiceAsync
    """

    def set_template_comment(
        self,
        request_body: SetTemplateCommentRequest,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().set_template_comment)(
            request_body, template_id, accept, request_config=request_config
        )
