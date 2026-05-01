from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import CreateEnvelopeRequest


class EnvelopeService(BaseService):
    """
    Service class for EnvelopeService operations.
    Provides methods to interact with EnvelopeService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._create_envelope_config: SdkConfig = {"environment": Environment.RESTAPI}

    def set_create_envelope_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_envelope.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_envelope_config = config
        return self

    @cast_models
    def create_envelope(
        self,
        request_body: CreateEnvelopeRequest,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """Create new envelope

        :param request_body: The request body.
        :type request_body: CreateEnvelopeRequest
        :param accept: accept
        :type accept: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(CreateEnvelopeRequest).is_nullable().validate(request_body)
        Validator(str).is_nullable().validate(accept)

        resolved_config = self._get_resolved_config(
            self._create_envelope_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.RESTAPI.url or Environment.DEFAULT.url}/envelope",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_header("Accept", accept)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response
