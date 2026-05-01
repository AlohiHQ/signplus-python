from typing import Any, Optional
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models


class TemplateTemplateIdAnnotationAnnotationIdService(BaseService):
    """
    Service class for TemplateTemplateIdAnnotationAnnotationIdService operations.
    Provides methods to interact with TemplateTemplateIdAnnotationAnnotationIdService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._delete_template_annotation_config: SdkConfig = {
            "environment": Environment.RESTAPI
        }

    def set_delete_template_annotation_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete_template_annotation.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_template_annotation_config = config
        return self

    @cast_models
    def delete_template_annotation(
        self,
        template_id: str,
        annotation_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """Delete template annotation

        :param template_id: template_id
        :type template_id: str
        :param annotation_id: annotation_id
        :type annotation_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(template_id)
        Validator(str).validate(annotation_id)

        resolved_config = self._get_resolved_config(
            self._delete_template_annotation_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.RESTAPI.url or Environment.DEFAULT.url}/template/{{template_id}}/annotation/{{annotation_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .add_path("annotation_id", annotation_id)
            .serialize()
            .set_method("DELETE")
        )

        response, _, _ = self.send_request(serialized_request)
        return response
