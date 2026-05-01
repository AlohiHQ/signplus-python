from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import SetTemplateCommentRequest


class TemplateTemplateIdSetCommentService(BaseService):
    """
    Service class for TemplateTemplateIdSetCommentService operations.
    Provides methods to interact with TemplateTemplateIdSetCommentService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._set_template_comment_config: SdkConfig = {
            "environment": Environment.RESTAPI
        }

    def set_set_template_comment_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set_template_comment.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_template_comment_config = config
        return self

    @cast_models
    def set_template_comment(
        self,
        request_body: SetTemplateCommentRequest,
        template_id: str,
        accept: Union[str, None],
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """Set template comment

        :param request_body: The request body.
        :type request_body: SetTemplateCommentRequest
        :param template_id: template_id
        :type template_id: str
        :param accept: accept
        :type accept: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(SetTemplateCommentRequest).is_nullable().validate(request_body)
        Validator(str).validate(template_id)
        Validator(str).is_nullable().validate(accept)

        resolved_config = self._get_resolved_config(
            self._set_template_comment_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.RESTAPI.url or Environment.DEFAULT.url}/template/{{template_id}}/set_comment",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_header("Accept", accept)
            .add_path("template_id", template_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return response
