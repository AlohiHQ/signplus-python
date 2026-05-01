from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models


class EnvelopeIdService(BaseService):
    """
    Service class for EnvelopeIdService operations.
    Provides methods to interact with EnvelopeIdService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._get_envelope_config: SdkConfig = {"environment": Environment.RESTAPI}
        self._delete_envelope_config: SdkConfig = {"environment": Environment.RESTAPI}

    def set_get_envelope_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_envelope.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_envelope_config = config
        return self

    def set_delete_envelope_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete_envelope.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_envelope_config = config
        return self

    @cast_models
    def get_envelope(
        self,
        envelope_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """Get envelope

        :param envelope_id: envelope_id
        :type envelope_id: str
        :param accept: accept
        :type accept: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(envelope_id)
        Validator(str).is_nullable().validate(accept)

        resolved_config = self._get_resolved_config(
            self._get_envelope_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.RESTAPI.url or Environment.DEFAULT.url}/envelope/{{envelope_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_header("Accept", accept)
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def delete_envelope(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Any:
        """Delete envelope

        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._delete_envelope_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.RESTAPI.url or Environment.DEFAULT.url}/envelope/{{envelope_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("DELETE")
        )

        response, _, _ = self.send_request(serialized_request)
        return response
