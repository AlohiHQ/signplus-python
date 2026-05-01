from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import ListWebhooksRequest


class WebhooksService(BaseService):
    """
    Service class for WebhooksService operations.
    Provides methods to interact with WebhooksService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._list_webhooks_config: SdkConfig = {"environment": Environment.RESTAPI}

    def set_list_webhooks_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list_webhooks.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_webhooks_config = config
        return self

    @cast_models
    def list_webhooks(
        self,
        request_body: ListWebhooksRequest,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """List webhooks

        :param request_body: The request body.
        :type request_body: ListWebhooksRequest
        :param accept: accept
        :type accept: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(ListWebhooksRequest).is_nullable().validate(request_body)
        Validator(str).is_nullable().validate(accept)

        resolved_config = self._get_resolved_config(
            self._list_webhooks_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.RESTAPI.url or Environment.DEFAULT.url}/webhooks",
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
