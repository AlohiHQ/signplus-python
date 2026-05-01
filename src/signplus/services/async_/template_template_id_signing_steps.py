from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..template_template_id_signing_steps import TemplateTemplateIdSigningStepsService
from ...net.sdk_config import SdkConfig
from ...models import AddTemplateSigningStepsRequest


class TemplateTemplateIdSigningStepsServiceAsync(TemplateTemplateIdSigningStepsService):
    """
    Async Wrapper for TemplateTemplateIdSigningStepsServiceAsync
    """

    def add_template_signing_steps(
        self,
        request_body: AddTemplateSigningStepsRequest,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().add_template_signing_steps)(
            request_body, template_id, accept, request_config=request_config
        )
