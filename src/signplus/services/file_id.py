from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models


class FileIdService(BaseService):
    """
    Service class for FileIdService operations.
    Provides methods to interact with FileIdService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._get_attachment_file_config: SdkConfig = {
            "environment": Environment.RESTAPI
        }

    def set_get_attachment_file_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_attachment_file.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_attachment_file_config = config
        return self

    @cast_models
    def get_attachment_file(
        self,
        envelope_id: str,
        file_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """Get envelope attachment file

        :param envelope_id: envelope_id
        :type envelope_id: str
        :param file_id: file_id
        :type file_id: str
        :param accept: accept
        :type accept: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(envelope_id)
        Validator(str).validate(file_id)
        Validator(str).is_nullable().validate(accept)

        resolved_config = self._get_resolved_config(
            self._get_attachment_file_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.RESTAPI.url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/attachments/{{file_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_header("Accept", accept)
            .add_path("envelope_id", envelope_id)
            .add_path("file_id", file_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response
