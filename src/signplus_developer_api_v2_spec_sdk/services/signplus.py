from typing import Any, Optional, List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.sdk_config import SdkConfig
from ..net.environment.environment import Environment
from ..models.utils.sentinel import SENTINEL
from ..models.utils.cast_models import cast_models
from ..models import (
    AddAnnotationRequest,
    AddEnvelopeDocumentRequest,
    AddEnvelopeSigningStepsRequest,
    AddTemplateDocumentRequest,
    AddTemplateSigningStepsRequest,
    Annotation,
    CreateEnvelopeFromTemplateRequest,
    CreateEnvelopeRequest,
    CreateTemplateRequest,
    CreateWebhookRequest,
    Document,
    Envelope,
    EnvelopeAttachments,
    EnvelopeNotification,
    ListEnvelopeDocumentAnnotationsResponse,
    ListEnvelopeDocumentsResponse,
    ListEnvelopesRequest,
    ListEnvelopesResponse,
    ListTemplateAnnotationsResponse,
    ListTemplateDocumentAnnotationsResponse,
    ListTemplateDocumentsResponse,
    ListTemplatesRequest,
    ListTemplatesResponse,
    ListWebhooksRequest,
    ListWebhooksResponse,
    RenameEnvelopeRequest,
    RenameTemplateRequest,
    SetEnvelopeAttachmentsPlaceholdersRequest,
    SetEnvelopeAttachmentsSettingsRequest,
    SetEnvelopeCommentRequest,
    SetEnvelopeDynamicFieldsRequest,
    SetEnvelopeExpirationRequest,
    SetEnvelopeLegalityLevelRequest,
    SetTemplateCommentRequest,
    Template,
    Webhook,
)


class SignplusService(BaseService):
    """
    Service class for SignplusService operations.
    Provides methods to interact with SignplusService-related API endpoints.
    Inherits common functionality from BaseService including authentication and request handling.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the service and method-level configurations."""
        super().__init__(*args, **kwargs)
        self._create_envelope_config: SdkConfig = {}
        self._create_envelope_from_template_config: SdkConfig = {}
        self._list_envelopes_config: SdkConfig = {}
        self._get_envelope_config: SdkConfig = {}
        self._delete_envelope_config: SdkConfig = {}
        self._download_envelope_signed_documents_config: SdkConfig = {}
        self._download_envelope_certificate_config: SdkConfig = {}
        self._get_envelope_document_config: SdkConfig = {}
        self._get_envelope_documents_config: SdkConfig = {}
        self._add_envelope_document_config: SdkConfig = {}
        self._set_envelope_dynamic_fields_config: SdkConfig = {}
        self._add_envelope_signing_steps_config: SdkConfig = {}
        self._set_envelope_attachments_settings_config: SdkConfig = {}
        self._set_envelope_attachments_placeholders_config: SdkConfig = {}
        self._get_attachment_file_config: SdkConfig = {}
        self._send_envelope_config: SdkConfig = {}
        self._duplicate_envelope_config: SdkConfig = {}
        self._void_envelope_config: SdkConfig = {}
        self._rename_envelope_config: SdkConfig = {}
        self._set_envelope_comment_config: SdkConfig = {}
        self._set_envelope_notification_config: SdkConfig = {}
        self._set_envelope_expiration_date_config: SdkConfig = {}
        self._set_envelope_legality_level_config: SdkConfig = {}
        self._get_envelope_annotations_config: SdkConfig = {}
        self._get_envelope_document_annotations_config: SdkConfig = {}
        self._add_envelope_annotation_config: SdkConfig = {}
        self._delete_envelope_annotation_config: SdkConfig = {}
        self._create_template_config: SdkConfig = {}
        self._list_templates_config: SdkConfig = {}
        self._get_template_config: SdkConfig = {}
        self._delete_template_config: SdkConfig = {}
        self._duplicate_template_config: SdkConfig = {}
        self._add_template_document_config: SdkConfig = {}
        self._get_template_document_config: SdkConfig = {}
        self._get_template_documents_config: SdkConfig = {}
        self._add_template_signing_steps_config: SdkConfig = {}
        self._rename_template_config: SdkConfig = {}
        self._set_template_comment_config: SdkConfig = {}
        self._set_template_notification_config: SdkConfig = {}
        self._get_template_annotations_config: SdkConfig = {}
        self._get_document_template_annotations_config: SdkConfig = {}
        self._add_template_annotation_config: SdkConfig = {}
        self._delete_template_annotation_config: SdkConfig = {}
        self._set_template_attachments_settings_config: SdkConfig = {}
        self._set_template_attachments_placeholders_config: SdkConfig = {}
        self._create_webhook_config: SdkConfig = {}
        self._list_webhooks_config: SdkConfig = {}
        self._delete_webhook_config: SdkConfig = {}

    def set_create_envelope_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_envelope.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_envelope_config = config
        return self

    def set_create_envelope_from_template_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_envelope_from_template.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_envelope_from_template_config = config
        return self

    def set_list_envelopes_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list_envelopes.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_envelopes_config = config
        return self

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

    def set_download_envelope_signed_documents_config(self, config: SdkConfig):
        """
        Sets method-level configuration for download_envelope_signed_documents.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._download_envelope_signed_documents_config = config
        return self

    def set_download_envelope_certificate_config(self, config: SdkConfig):
        """
        Sets method-level configuration for download_envelope_certificate.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._download_envelope_certificate_config = config
        return self

    def set_get_envelope_document_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_envelope_document.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_envelope_document_config = config
        return self

    def set_get_envelope_documents_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_envelope_documents.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_envelope_documents_config = config
        return self

    def set_add_envelope_document_config(self, config: SdkConfig):
        """
        Sets method-level configuration for add_envelope_document.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._add_envelope_document_config = config
        return self

    def set_set_envelope_dynamic_fields_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set_envelope_dynamic_fields.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_envelope_dynamic_fields_config = config
        return self

    def set_add_envelope_signing_steps_config(self, config: SdkConfig):
        """
        Sets method-level configuration for add_envelope_signing_steps.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._add_envelope_signing_steps_config = config
        return self

    def set_set_envelope_attachments_settings_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set_envelope_attachments_settings.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_envelope_attachments_settings_config = config
        return self

    def set_set_envelope_attachments_placeholders_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set_envelope_attachments_placeholders.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_envelope_attachments_placeholders_config = config
        return self

    def set_get_attachment_file_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_attachment_file.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_attachment_file_config = config
        return self

    def set_send_envelope_config(self, config: SdkConfig):
        """
        Sets method-level configuration for send_envelope.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._send_envelope_config = config
        return self

    def set_duplicate_envelope_config(self, config: SdkConfig):
        """
        Sets method-level configuration for duplicate_envelope.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._duplicate_envelope_config = config
        return self

    def set_void_envelope_config(self, config: SdkConfig):
        """
        Sets method-level configuration for void_envelope.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._void_envelope_config = config
        return self

    def set_rename_envelope_config(self, config: SdkConfig):
        """
        Sets method-level configuration for rename_envelope.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._rename_envelope_config = config
        return self

    def set_set_envelope_comment_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set_envelope_comment.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_envelope_comment_config = config
        return self

    def set_set_envelope_notification_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set_envelope_notification.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_envelope_notification_config = config
        return self

    def set_set_envelope_expiration_date_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set_envelope_expiration_date.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_envelope_expiration_date_config = config
        return self

    def set_set_envelope_legality_level_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set_envelope_legality_level.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_envelope_legality_level_config = config
        return self

    def set_get_envelope_annotations_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_envelope_annotations.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_envelope_annotations_config = config
        return self

    def set_get_envelope_document_annotations_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_envelope_document_annotations.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_envelope_document_annotations_config = config
        return self

    def set_add_envelope_annotation_config(self, config: SdkConfig):
        """
        Sets method-level configuration for add_envelope_annotation.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._add_envelope_annotation_config = config
        return self

    def set_delete_envelope_annotation_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete_envelope_annotation.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_envelope_annotation_config = config
        return self

    def set_create_template_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_template.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_template_config = config
        return self

    def set_list_templates_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list_templates.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_templates_config = config
        return self

    def set_get_template_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_template.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_template_config = config
        return self

    def set_delete_template_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete_template.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_template_config = config
        return self

    def set_duplicate_template_config(self, config: SdkConfig):
        """
        Sets method-level configuration for duplicate_template.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._duplicate_template_config = config
        return self

    def set_add_template_document_config(self, config: SdkConfig):
        """
        Sets method-level configuration for add_template_document.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._add_template_document_config = config
        return self

    def set_get_template_document_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_template_document.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_template_document_config = config
        return self

    def set_get_template_documents_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_template_documents.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_template_documents_config = config
        return self

    def set_add_template_signing_steps_config(self, config: SdkConfig):
        """
        Sets method-level configuration for add_template_signing_steps.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._add_template_signing_steps_config = config
        return self

    def set_rename_template_config(self, config: SdkConfig):
        """
        Sets method-level configuration for rename_template.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._rename_template_config = config
        return self

    def set_set_template_comment_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set_template_comment.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_template_comment_config = config
        return self

    def set_set_template_notification_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set_template_notification.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_template_notification_config = config
        return self

    def set_get_template_annotations_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_template_annotations.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_template_annotations_config = config
        return self

    def set_get_document_template_annotations_config(self, config: SdkConfig):
        """
        Sets method-level configuration for get_document_template_annotations.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._get_document_template_annotations_config = config
        return self

    def set_add_template_annotation_config(self, config: SdkConfig):
        """
        Sets method-level configuration for add_template_annotation.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._add_template_annotation_config = config
        return self

    def set_delete_template_annotation_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete_template_annotation.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_template_annotation_config = config
        return self

    def set_set_template_attachments_settings_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set_template_attachments_settings.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_template_attachments_settings_config = config
        return self

    def set_set_template_attachments_placeholders_config(self, config: SdkConfig):
        """
        Sets method-level configuration for set_template_attachments_placeholders.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._set_template_attachments_placeholders_config = config
        return self

    def set_create_webhook_config(self, config: SdkConfig):
        """
        Sets method-level configuration for create_webhook.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._create_webhook_config = config
        return self

    def set_list_webhooks_config(self, config: SdkConfig):
        """
        Sets method-level configuration for list_webhooks.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._list_webhooks_config = config
        return self

    def set_delete_webhook_config(self, config: SdkConfig):
        """
        Sets method-level configuration for delete_webhook.

        :param SdkConfig config: Configuration dictionary to override service-level defaults.
        :return: The service instance for method chaining.
        """
        self._delete_webhook_config = config
        return self

    @cast_models
    def create_envelope(
        self,
        request_body: CreateEnvelopeRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Envelope:
        """Create new envelope

        :param request_body: The request body.
        :type request_body: CreateEnvelopeRequest
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Envelope
        """

        Validator(CreateEnvelopeRequest).validate(request_body)

        resolved_config = self._get_resolved_config(
            self._create_envelope_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Envelope.model_validate(response)

    @cast_models
    def create_envelope_from_template(
        self,
        request_body: CreateEnvelopeFromTemplateRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Envelope:
        """Create new envelope from template

        :param request_body: The request body.
        :type request_body: CreateEnvelopeFromTemplateRequest
        :param template_id: template_id
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Envelope
        """

        Validator(CreateEnvelopeFromTemplateRequest).validate(request_body)
        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._create_envelope_from_template_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/from_template/{{template_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Envelope.model_validate(response)

    @cast_models
    def list_envelopes(
        self,
        request_body: ListEnvelopesRequest = None,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> ListEnvelopesResponse:
        """List envelopes

        :param request_body: The request body., defaults to None
        :type request_body: ListEnvelopesRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ListEnvelopesResponse
        """

        Validator(ListEnvelopesRequest).is_optional().validate(request_body)

        resolved_config = self._get_resolved_config(
            self._list_envelopes_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelopes",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return ListEnvelopesResponse.model_validate(response)

    @cast_models
    def get_envelope(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Envelope:
        """Get envelope

        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Envelope
        """

        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._get_envelope_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return Envelope.model_validate(response)

    @cast_models
    def delete_envelope(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> None:
        """Delete envelope

        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._delete_envelope_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("DELETE")
        )

        self.send_request(serialized_request)

    @cast_models
    def download_envelope_signed_documents(
        self,
        envelope_id: str,
        certificate_of_completion: bool = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> any:
        """Download signed documents for an envelope

        :param envelope_id: ID of the envelope
        :type envelope_id: str
        :param certificate_of_completion: Whether to include the certificate of completion in the downloaded file, defaults to None
        :type certificate_of_completion: bool, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        Validator(str).validate(envelope_id)
        Validator(bool).is_optional().validate(certificate_of_completion)

        resolved_config = self._get_resolved_config(
            self._download_envelope_signed_documents_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/signed_documents",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .add_query("certificate_of_completion", certificate_of_completion)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def download_envelope_certificate(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> any:
        """Download certificate of completion for an envelope

        :param envelope_id: ID of the envelope
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: any
        """

        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._download_envelope_certificate_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/certificate",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def get_envelope_document(
        self,
        envelope_id: str,
        document_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Document:
        """Get envelope document

        :param envelope_id: envelope_id
        :type envelope_id: str
        :param document_id: document_id
        :type document_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Document
        """

        Validator(str).validate(envelope_id)
        Validator(str).validate(document_id)

        resolved_config = self._get_resolved_config(
            self._get_envelope_document_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/document/{{document_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .add_path("document_id", document_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return Document.model_validate(response)

    @cast_models
    def get_envelope_documents(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> ListEnvelopeDocumentsResponse:
        """Get envelope documents

        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ListEnvelopeDocumentsResponse
        """

        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._get_envelope_documents_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/documents",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return ListEnvelopeDocumentsResponse.model_validate(response)

    @cast_models
    def add_envelope_document(
        self,
        request_body: AddEnvelopeDocumentRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Document:
        """Add envelope document

        :param request_body: The request body.
        :type request_body: AddEnvelopeDocumentRequest
        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Document
        """

        Validator(AddEnvelopeDocumentRequest).validate(request_body)
        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._add_envelope_document_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/document",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, _, _ = self.send_request(serialized_request)
        return Document.model_validate(response)

    @cast_models
    def set_envelope_dynamic_fields(
        self,
        request_body: SetEnvelopeDynamicFieldsRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Envelope:
        """Set envelope dynamic fields

        :param request_body: The request body.
        :type request_body: SetEnvelopeDynamicFieldsRequest
        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Envelope
        """

        Validator(SetEnvelopeDynamicFieldsRequest).validate(request_body)
        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._set_envelope_dynamic_fields_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/dynamic_fields",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Envelope.model_validate(response)

    @cast_models
    def add_envelope_signing_steps(
        self,
        request_body: AddEnvelopeSigningStepsRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Envelope:
        """Add envelope signing steps

        :param request_body: The request body.
        :type request_body: AddEnvelopeSigningStepsRequest
        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Envelope
        """

        Validator(AddEnvelopeSigningStepsRequest).validate(request_body)
        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._add_envelope_signing_steps_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/signing_steps",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Envelope.model_validate(response)

    @cast_models
    def set_envelope_attachments_settings(
        self,
        request_body: SetEnvelopeAttachmentsSettingsRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> EnvelopeAttachments:
        """Set envelope attachment settings

        :param request_body: The request body.
        :type request_body: SetEnvelopeAttachmentsSettingsRequest
        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: EnvelopeAttachments
        """

        Validator(SetEnvelopeAttachmentsSettingsRequest).validate(request_body)
        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._set_envelope_attachments_settings_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/attachments/settings",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return EnvelopeAttachments.model_validate(response)

    @cast_models
    def set_envelope_attachments_placeholders(
        self,
        request_body: SetEnvelopeAttachmentsPlaceholdersRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> EnvelopeAttachments:
        """Placeholders to be set, completely replacing the existing ones.

        :param request_body: The request body.
        :type request_body: SetEnvelopeAttachmentsPlaceholdersRequest
        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: EnvelopeAttachments
        """

        Validator(SetEnvelopeAttachmentsPlaceholdersRequest).validate(request_body)
        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._set_envelope_attachments_placeholders_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/attachments/placeholders",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return EnvelopeAttachments.model_validate(response)

    @cast_models
    def get_attachment_file(
        self,
        envelope_id: str,
        file_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> bytes:
        """Get envelope attachment file

        :param envelope_id: envelope_id
        :type envelope_id: str
        :param file_id: file_id
        :type file_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: bytes
        """

        Validator(str).validate(envelope_id)
        Validator(str).validate(file_id)

        resolved_config = self._get_resolved_config(
            self._get_attachment_file_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/attachments/{{file_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .add_path("file_id", file_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return response

    @cast_models
    def send_envelope(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Envelope:
        """Send envelope for signature

        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Envelope
        """

        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._send_envelope_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/send",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("POST")
        )

        response, _, _ = self.send_request(serialized_request)
        return Envelope.model_validate(response)

    @cast_models
    def duplicate_envelope(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Envelope:
        """Duplicate envelope

        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Envelope
        """

        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._duplicate_envelope_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/duplicate",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("POST")
        )

        response, _, _ = self.send_request(serialized_request)
        return Envelope.model_validate(response)

    @cast_models
    def void_envelope(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Envelope:
        """Void envelope

        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Envelope
        """

        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._void_envelope_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/void",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("PUT")
        )

        response, _, _ = self.send_request(serialized_request)
        return Envelope.model_validate(response)

    @cast_models
    def rename_envelope(
        self,
        request_body: RenameEnvelopeRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Envelope:
        """Rename envelope

        :param request_body: The request body.
        :type request_body: RenameEnvelopeRequest
        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Envelope
        """

        Validator(RenameEnvelopeRequest).validate(request_body)
        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._rename_envelope_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/rename",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Envelope.model_validate(response)

    @cast_models
    def set_envelope_comment(
        self,
        request_body: SetEnvelopeCommentRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Envelope:
        """Set envelope comment

        :param request_body: The request body.
        :type request_body: SetEnvelopeCommentRequest
        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Envelope
        """

        Validator(SetEnvelopeCommentRequest).validate(request_body)
        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._set_envelope_comment_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/set_comment",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Envelope.model_validate(response)

    @cast_models
    def set_envelope_notification(
        self,
        request_body: EnvelopeNotification,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Envelope:
        """Set envelope notification

        :param request_body: The request body.
        :type request_body: EnvelopeNotification
        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Envelope
        """

        Validator(EnvelopeNotification).validate(request_body)
        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._set_envelope_notification_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/set_notification",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Envelope.model_validate(response)

    @cast_models
    def set_envelope_expiration_date(
        self,
        request_body: SetEnvelopeExpirationRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Envelope:
        """Set envelope expiration date

        :param request_body: The request body.
        :type request_body: SetEnvelopeExpirationRequest
        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Envelope
        """

        Validator(SetEnvelopeExpirationRequest).validate(request_body)
        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._set_envelope_expiration_date_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/set_expiration_date",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Envelope.model_validate(response)

    @cast_models
    def set_envelope_legality_level(
        self,
        request_body: SetEnvelopeLegalityLevelRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Envelope:
        """Set envelope legality level

        :param request_body: The request body.
        :type request_body: SetEnvelopeLegalityLevelRequest
        :param envelope_id: envelope_id
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Envelope
        """

        Validator(SetEnvelopeLegalityLevelRequest).validate(request_body)
        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._set_envelope_legality_level_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/set_legality_level",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Envelope.model_validate(response)

    @cast_models
    def get_envelope_annotations(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> List[Annotation]:
        """Get envelope annotations

        :param envelope_id: ID of the envelope
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: List[Annotation]
        """

        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._get_envelope_annotations_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/annotations",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return [Annotation.model_validate(item) for item in response]

    @cast_models
    def get_envelope_document_annotations(
        self,
        envelope_id: str,
        document_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> ListEnvelopeDocumentAnnotationsResponse:
        """Get envelope document annotations

        :param envelope_id: ID of the envelope
        :type envelope_id: str
        :param document_id: ID of document
        :type document_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ListEnvelopeDocumentAnnotationsResponse
        """

        Validator(str).validate(envelope_id)
        Validator(str).validate(document_id)

        resolved_config = self._get_resolved_config(
            self._get_envelope_document_annotations_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/annotations/{{document_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .add_path("document_id", document_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return ListEnvelopeDocumentAnnotationsResponse.model_validate(response)

    @cast_models
    def add_envelope_annotation(
        self,
        request_body: AddAnnotationRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Annotation:
        """Add envelope annotation

        :param request_body: The request body.
        :type request_body: AddAnnotationRequest
        :param envelope_id: ID of the envelope
        :type envelope_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Annotation
        """

        Validator(AddAnnotationRequest).validate(request_body)
        Validator(str).validate(envelope_id)

        resolved_config = self._get_resolved_config(
            self._add_envelope_annotation_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/annotation",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Annotation.model_validate(response)

    @cast_models
    def delete_envelope_annotation(
        self,
        envelope_id: str,
        annotation_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> None:
        """Delete envelope annotation

        :param envelope_id: ID of the envelope
        :type envelope_id: str
        :param annotation_id: ID of the annotation to delete
        :type annotation_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(envelope_id)
        Validator(str).validate(annotation_id)

        resolved_config = self._get_resolved_config(
            self._delete_envelope_annotation_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/envelope/{{envelope_id}}/annotation/{{annotation_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("envelope_id", envelope_id)
            .add_path("annotation_id", annotation_id)
            .serialize()
            .set_method("DELETE")
        )

        self.send_request(serialized_request)

    @cast_models
    def create_template(
        self,
        request_body: CreateTemplateRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Template:
        """Create new template

        :param request_body: The request body.
        :type request_body: CreateTemplateRequest
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Template
        """

        Validator(CreateTemplateRequest).validate(request_body)

        resolved_config = self._get_resolved_config(
            self._create_template_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Template.model_validate(response)

    @cast_models
    def list_templates(
        self,
        request_body: ListTemplatesRequest = None,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> ListTemplatesResponse:
        """List templates

        :param request_body: The request body., defaults to None
        :type request_body: ListTemplatesRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ListTemplatesResponse
        """

        Validator(ListTemplatesRequest).is_optional().validate(request_body)

        resolved_config = self._get_resolved_config(
            self._list_templates_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/templates",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return ListTemplatesResponse.model_validate(response)

    @cast_models
    def get_template(
        self, template_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Template:
        """Get template

        :param template_id: template_id
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Template
        """

        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._get_template_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return Template.model_validate(response)

    @cast_models
    def delete_template(
        self, template_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> None:
        """Delete template

        :param template_id: template_id
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._delete_template_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("DELETE")
        )

        self.send_request(serialized_request)

    @cast_models
    def duplicate_template(
        self, template_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Template:
        """Duplicate template

        :param template_id: template_id
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Template
        """

        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._duplicate_template_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/duplicate",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("POST")
        )

        response, _, _ = self.send_request(serialized_request)
        return Template.model_validate(response)

    @cast_models
    def add_template_document(
        self,
        request_body: AddTemplateDocumentRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Document:
        """Add template document

        :param request_body: The request body.
        :type request_body: AddTemplateDocumentRequest
        :param template_id: template_id
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Document
        """

        Validator(AddTemplateDocumentRequest).validate(request_body)
        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._add_template_document_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/document",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body, "multipart/form-data")
        )

        response, _, _ = self.send_request(serialized_request)
        return Document.model_validate(response)

    @cast_models
    def get_template_document(
        self,
        template_id: str,
        document_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Document:
        """Get template document

        :param template_id: template_id
        :type template_id: str
        :param document_id: document_id
        :type document_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Document
        """

        Validator(str).validate(template_id)
        Validator(str).validate(document_id)

        resolved_config = self._get_resolved_config(
            self._get_template_document_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/document/{{document_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .add_path("document_id", document_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return Document.model_validate(response)

    @cast_models
    def get_template_documents(
        self, template_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> ListTemplateDocumentsResponse:
        """Get template documents

        :param template_id: template_id
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ListTemplateDocumentsResponse
        """

        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._get_template_documents_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/documents",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return ListTemplateDocumentsResponse.model_validate(response)

    @cast_models
    def add_template_signing_steps(
        self,
        request_body: AddTemplateSigningStepsRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Template:
        """Add template signing steps

        :param request_body: The request body.
        :type request_body: AddTemplateSigningStepsRequest
        :param template_id: template_id
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Template
        """

        Validator(AddTemplateSigningStepsRequest).validate(request_body)
        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._add_template_signing_steps_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/signing_steps",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Template.model_validate(response)

    @cast_models
    def rename_template(
        self,
        request_body: RenameTemplateRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Template:
        """Rename template

        :param request_body: The request body.
        :type request_body: RenameTemplateRequest
        :param template_id: template_id
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Template
        """

        Validator(RenameTemplateRequest).validate(request_body)
        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._rename_template_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/rename",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Template.model_validate(response)

    @cast_models
    def set_template_comment(
        self,
        request_body: SetTemplateCommentRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Template:
        """Set template comment

        :param request_body: The request body.
        :type request_body: SetTemplateCommentRequest
        :param template_id: template_id
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Template
        """

        Validator(SetTemplateCommentRequest).validate(request_body)
        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._set_template_comment_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/set_comment",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Template.model_validate(response)

    @cast_models
    def set_template_notification(
        self,
        request_body: EnvelopeNotification,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Template:
        """Set template notification

        :param request_body: The request body.
        :type request_body: EnvelopeNotification
        :param template_id: template_id
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Template
        """

        Validator(EnvelopeNotification).validate(request_body)
        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._set_template_notification_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/set_notification",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Template.model_validate(response)

    @cast_models
    def get_template_annotations(
        self, template_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> ListTemplateAnnotationsResponse:
        """Get template annotations

        :param template_id: ID of the template
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ListTemplateAnnotationsResponse
        """

        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._get_template_annotations_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/annotations",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return ListTemplateAnnotationsResponse.model_validate(response)

    @cast_models
    def get_document_template_annotations(
        self,
        template_id: str,
        document_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> ListTemplateDocumentAnnotationsResponse:
        """Get document template annotations

        :param template_id: ID of the template
        :type template_id: str
        :param document_id: ID of document
        :type document_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ListTemplateDocumentAnnotationsResponse
        """

        Validator(str).validate(template_id)
        Validator(str).validate(document_id)

        resolved_config = self._get_resolved_config(
            self._get_document_template_annotations_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/annotations/{{document_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .add_path("document_id", document_id)
            .serialize()
            .set_method("GET")
        )

        response, _, _ = self.send_request(serialized_request)
        return ListTemplateDocumentAnnotationsResponse.model_validate(response)

    @cast_models
    def add_template_annotation(
        self,
        request_body: AddAnnotationRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Annotation:
        """Add template annotation

        :param request_body: The request body.
        :type request_body: AddAnnotationRequest
        :param template_id: ID of the template
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Annotation
        """

        Validator(AddAnnotationRequest).validate(request_body)
        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._add_template_annotation_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/annotation",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Annotation.model_validate(response)

    @cast_models
    def delete_template_annotation(
        self,
        template_id: str,
        annotation_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> None:
        """Delete template annotation

        :param template_id: ID of the template
        :type template_id: str
        :param annotation_id: ID of the annotation to delete
        :type annotation_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(template_id)
        Validator(str).validate(annotation_id)

        resolved_config = self._get_resolved_config(
            self._delete_template_annotation_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/annotation/{{annotation_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .add_path("annotation_id", annotation_id)
            .serialize()
            .set_method("DELETE")
        )

        self.send_request(serialized_request)

    @cast_models
    def set_template_attachments_settings(
        self,
        request_body: SetEnvelopeAttachmentsSettingsRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> EnvelopeAttachments:
        """Set template attachment settings

        :param request_body: The request body.
        :type request_body: SetEnvelopeAttachmentsSettingsRequest
        :param template_id: template_id
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: EnvelopeAttachments
        """

        Validator(SetEnvelopeAttachmentsSettingsRequest).validate(request_body)
        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._set_template_attachments_settings_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/attachments/settings",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return EnvelopeAttachments.model_validate(response)

    @cast_models
    def set_template_attachments_placeholders(
        self,
        request_body: SetEnvelopeAttachmentsPlaceholdersRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> EnvelopeAttachments:
        """Placeholders to be set, completely replacing the existing ones.

        :param request_body: The request body.
        :type request_body: SetEnvelopeAttachmentsPlaceholdersRequest
        :param template_id: template_id
        :type template_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: EnvelopeAttachments
        """

        Validator(SetEnvelopeAttachmentsPlaceholdersRequest).validate(request_body)
        Validator(str).validate(template_id)

        resolved_config = self._get_resolved_config(
            self._set_template_attachments_placeholders_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/template/{{template_id}}/attachments/placeholders",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("template_id", template_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return EnvelopeAttachments.model_validate(response)

    @cast_models
    def create_webhook(
        self,
        request_body: CreateWebhookRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Webhook:
        """Create webhook

        :param request_body: The request body.
        :type request_body: CreateWebhookRequest
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Webhook
        """

        Validator(CreateWebhookRequest).validate(request_body)

        resolved_config = self._get_resolved_config(
            self._create_webhook_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/webhook",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return Webhook.model_validate(response)

    @cast_models
    def list_webhooks(
        self,
        request_body: ListWebhooksRequest = None,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> ListWebhooksResponse:
        """List webhooks

        :param request_body: The request body., defaults to None
        :type request_body: ListWebhooksRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: ListWebhooksResponse
        """

        Validator(ListWebhooksRequest).is_optional().validate(request_body)

        resolved_config = self._get_resolved_config(
            self._list_webhooks_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/webhooks",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, _, _ = self.send_request(serialized_request)
        return ListWebhooksResponse.model_validate(response)

    @cast_models
    def delete_webhook(
        self, webhook_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> None:
        """Delete webhook

        :param webhook_id: webhook_id
        :type webhook_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(webhook_id)

        resolved_config = self._get_resolved_config(
            self._delete_webhook_config, request_config
        )

        serialized_request = (
            Serializer(
                f"{resolved_config.get('base_url') or self.base_url or Environment.DEFAULT.url}/webhook/{{webhook_id}}",
                [self.get_access_token(resolved_config)],
                resolved_config,
            )
            .add_path("webhook_id", webhook_id)
            .serialize()
            .set_method("DELETE")
        )

        self.send_request(serialized_request)
