from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..certificate import CertificateService
from ...net.sdk_config import SdkConfig


class CertificateServiceAsync(CertificateService):
    """
    Async Wrapper for CertificateServiceAsync
    """

    def download_envelope_certificate(
        self,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().download_envelope_certificate)(
            envelope_id, accept, request_config=request_config
        )
