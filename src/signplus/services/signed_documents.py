from typing import Any, Optional, Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models


class SignedDocumentsService(BaseService):
    """
    Service class for SignedDocumentsService operations.
    Provides methods to interact with SignedDocumentsService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._download_envelope_signed_documents_config: SdkConfig = {
            "environment": Environment.RESTAPI
        }

    def set_download_envelope_signed_documents_config(self, config: SdkConfig):
        """
        Sets method-level configuration for download_envelope_signed_documents.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._download_envelope_signed_documents_config = config
        return self

    @cast_models
    def download_envelope_signed_documents(
        self,
        envelope_id: str,
        accept: Union[str, None],
        certificate_of_completion: Union[str, None] = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Any:
        """Download signed documents for an envelope

        :param envelope_id: envelope_id
        :type envelope_id: str
        :param accept: accept
        :type accept: str
        :param certificate_of_completion: Whether to include the certificate of completion in the downloaded file, defaults to None
        :type certificate_of_completion: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Any
        """

        Validator(str).validate(envelope_id)
        Validator(str).is_nullable().validate(accept)
        Validator(str).is_optional().is_nullable().validate(certificate_of_completion)

        resolved_config = self._get_resolved_config(
            self._download_envelope_signed_documents_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.RESTAPI.url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/signed_documents",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_header("Accept", accept)
            .add_path("envelope_id", envelope_id)
            .add_query(
                "certificate_of_completion", certificate_of_completion, nullable=True
            )
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response
