from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id_rename import TemplateTemplateIdRenameService
from ...net.sdk_config import SdkConfig
from ...models import RenameTemplateRequest


class TemplateTemplateIdRenameServiceAsync(TemplateTemplateIdRenameService):
    """
    Async Wrapper for TemplateTemplateIdRenameServiceAsync
    """

    def rename_template(
        self,
        request_body: RenameTemplateRequest,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().rename_template)(
            request_body, template_id, accept, request_config=request_config
        )
