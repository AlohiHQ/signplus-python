from typing import Awaitable, Optional, Any, Union
from .utils.to_async import to_async
from ..file_id import FileIdService
from ...net.sdk_config import SdkConfig


class FileIdServiceAsync(FileIdService):
    """
    Async Wrapper for FileIdServiceAsync
    """

    def get_attachment_file(
        self,
        envelope_id: str,
        file_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().get_attachment_file)(
            envelope_id, file_id, accept, request_config=request_config
        )
