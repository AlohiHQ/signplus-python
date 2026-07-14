from typing import Awaitable, Optional, Any, List
from .utils.to_async import to_async
from ..signplus import SignplusService
from ...net.sdk_config import SdkConfig
from ...models.utils.sentinel import SENTINEL
from ...models import (
    Envelope,
    CreateEnvelopeRequest,
    CreateEnvelopeFromTemplateRequest,
    ListEnvelopesResponse,
    ListEnvelopesRequest,
    Document,
    ListEnvelopeDocumentsResponse,
    AddEnvelopeDocumentRequest,
    SetEnvelopeDynamicFieldsRequest,
    AddEnvelopeSigningStepsRequest,
    EnvelopeAttachments,
    SetEnvelopeAttachmentsSettingsRequest,
    SetEnvelopeAttachmentsPlaceholdersRequest,
    RenameEnvelopeRequest,
    SetEnvelopeCommentRequest,
    EnvelopeNotification,
    SetEnvelopeExpirationRequest,
    SetEnvelopeLegalityLevelRequest,
    Annotation,
    ListEnvelopeDocumentAnnotationsResponse,
    AddAnnotationRequest,
    Template,
    CreateTemplateRequest,
    ListTemplatesResponse,
    ListTemplatesRequest,
    AddTemplateDocumentRequest,
    ListTemplateDocumentsResponse,
    AddTemplateSigningStepsRequest,
    RenameTemplateRequest,
    SetTemplateCommentRequest,
    ListTemplateAnnotationsResponse,
    ListTemplateDocumentAnnotationsResponse,
    Webhook,
    CreateWebhookRequest,
    ListWebhooksResponse,
    ListWebhooksRequest,
)


class SignplusServiceAsync(SignplusService):
    """
    Async Wrapper for SignplusServiceAsync
    """

    def create_envelope(
        self,
        request_body: CreateEnvelopeRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Envelope]:
        return to_async(super().create_envelope)(
            request_body, request_config=request_config
        )

    def create_envelope_from_template(
        self,
        request_body: CreateEnvelopeFromTemplateRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Envelope]:
        return to_async(super().create_envelope_from_template)(
            request_body, template_id, request_config=request_config
        )

    def list_envelopes(
        self,
        request_body: ListEnvelopesRequest = None,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[ListEnvelopesResponse]:
        return to_async(super().list_envelopes)(
            request_body, request_config=request_config
        )

    def get_envelope(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Envelope]:
        return to_async(super().get_envelope)(
            envelope_id, request_config=request_config
        )

    def delete_envelope(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[None]:
        return to_async(super().delete_envelope)(
            envelope_id, request_config=request_config
        )

    def download_envelope_signed_documents(
        self,
        envelope_id: str,
        certificate_of_completion: bool = SENTINEL,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Any]:
        return to_async(super().download_envelope_signed_documents)(
            envelope_id, certificate_of_completion, request_config=request_config
        )

    def download_envelope_certificate(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Any]:
        return to_async(super().download_envelope_certificate)(
            envelope_id, request_config=request_config
        )

    def get_envelope_document(
        self,
        envelope_id: str,
        document_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Document]:
        return to_async(super().get_envelope_document)(
            envelope_id, document_id, request_config=request_config
        )

    def get_envelope_documents(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[ListEnvelopeDocumentsResponse]:
        return to_async(super().get_envelope_documents)(
            envelope_id, request_config=request_config
        )

    def add_envelope_document(
        self,
        request_body: AddEnvelopeDocumentRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Document]:
        return to_async(super().add_envelope_document)(
            request_body, envelope_id, request_config=request_config
        )

    def set_envelope_dynamic_fields(
        self,
        request_body: SetEnvelopeDynamicFieldsRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Envelope]:
        return to_async(super().set_envelope_dynamic_fields)(
            request_body, envelope_id, request_config=request_config
        )

    def add_envelope_signing_steps(
        self,
        request_body: AddEnvelopeSigningStepsRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Envelope]:
        return to_async(super().add_envelope_signing_steps)(
            request_body, envelope_id, request_config=request_config
        )

    def set_envelope_attachments_settings(
        self,
        request_body: SetEnvelopeAttachmentsSettingsRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[EnvelopeAttachments]:
        return to_async(super().set_envelope_attachments_settings)(
            request_body, envelope_id, request_config=request_config
        )

    def set_envelope_attachments_placeholders(
        self,
        request_body: SetEnvelopeAttachmentsPlaceholdersRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[EnvelopeAttachments]:
        return to_async(super().set_envelope_attachments_placeholders)(
            request_body, envelope_id, request_config=request_config
        )

    def get_attachment_file(
        self,
        envelope_id: str,
        file_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[bytes]:
        return to_async(super().get_attachment_file)(
            envelope_id, file_id, request_config=request_config
        )

    def send_envelope(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Envelope]:
        return to_async(super().send_envelope)(
            envelope_id, request_config=request_config
        )

    def duplicate_envelope(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Envelope]:
        return to_async(super().duplicate_envelope)(
            envelope_id, request_config=request_config
        )

    def void_envelope(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Envelope]:
        return to_async(super().void_envelope)(
            envelope_id, request_config=request_config
        )

    def rename_envelope(
        self,
        request_body: RenameEnvelopeRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Envelope]:
        return to_async(super().rename_envelope)(
            request_body, envelope_id, request_config=request_config
        )

    def set_envelope_comment(
        self,
        request_body: SetEnvelopeCommentRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Envelope]:
        return to_async(super().set_envelope_comment)(
            request_body, envelope_id, request_config=request_config
        )

    def set_envelope_notification(
        self,
        request_body: EnvelopeNotification,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Envelope]:
        return to_async(super().set_envelope_notification)(
            request_body, envelope_id, request_config=request_config
        )

    def set_envelope_expiration_date(
        self,
        request_body: SetEnvelopeExpirationRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Envelope]:
        return to_async(super().set_envelope_expiration_date)(
            request_body, envelope_id, request_config=request_config
        )

    def set_envelope_legality_level(
        self,
        request_body: SetEnvelopeLegalityLevelRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Envelope]:
        return to_async(super().set_envelope_legality_level)(
            request_body, envelope_id, request_config=request_config
        )

    def get_envelope_annotations(
        self, envelope_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[List[Annotation]]:
        return to_async(super().get_envelope_annotations)(
            envelope_id, request_config=request_config
        )

    def get_envelope_document_annotations(
        self,
        envelope_id: str,
        document_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[ListEnvelopeDocumentAnnotationsResponse]:
        return to_async(super().get_envelope_document_annotations)(
            envelope_id, document_id, request_config=request_config
        )

    def add_envelope_annotation(
        self,
        request_body: AddAnnotationRequest,
        envelope_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Annotation]:
        return to_async(super().add_envelope_annotation)(
            request_body, envelope_id, request_config=request_config
        )

    def delete_envelope_annotation(
        self,
        envelope_id: str,
        annotation_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[None]:
        return to_async(super().delete_envelope_annotation)(
            envelope_id, annotation_id, request_config=request_config
        )

    def create_template(
        self,
        request_body: CreateTemplateRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Template]:
        return to_async(super().create_template)(
            request_body, request_config=request_config
        )

    def list_templates(
        self,
        request_body: ListTemplatesRequest = None,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[ListTemplatesResponse]:
        return to_async(super().list_templates)(
            request_body, request_config=request_config
        )

    def get_template(
        self, template_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Template]:
        return to_async(super().get_template)(
            template_id, request_config=request_config
        )

    def delete_template(
        self, template_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[None]:
        return to_async(super().delete_template)(
            template_id, request_config=request_config
        )

    def duplicate_template(
        self, template_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[Template]:
        return to_async(super().duplicate_template)(
            template_id, request_config=request_config
        )

    def add_template_document(
        self,
        request_body: AddTemplateDocumentRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Document]:
        return to_async(super().add_template_document)(
            request_body, template_id, request_config=request_config
        )

    def get_template_document(
        self,
        template_id: str,
        document_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Document]:
        return to_async(super().get_template_document)(
            template_id, document_id, request_config=request_config
        )

    def get_template_documents(
        self, template_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[ListTemplateDocumentsResponse]:
        return to_async(super().get_template_documents)(
            template_id, request_config=request_config
        )

    def add_template_signing_steps(
        self,
        request_body: AddTemplateSigningStepsRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Template]:
        return to_async(super().add_template_signing_steps)(
            request_body, template_id, request_config=request_config
        )

    def rename_template(
        self,
        request_body: RenameTemplateRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Template]:
        return to_async(super().rename_template)(
            request_body, template_id, request_config=request_config
        )

    def set_template_comment(
        self,
        request_body: SetTemplateCommentRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Template]:
        return to_async(super().set_template_comment)(
            request_body, template_id, request_config=request_config
        )

    def set_template_notification(
        self,
        request_body: EnvelopeNotification,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Template]:
        return to_async(super().set_template_notification)(
            request_body, template_id, request_config=request_config
        )

    def get_template_annotations(
        self, template_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[ListTemplateAnnotationsResponse]:
        return to_async(super().get_template_annotations)(
            template_id, request_config=request_config
        )

    def get_document_template_annotations(
        self,
        template_id: str,
        document_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[ListTemplateDocumentAnnotationsResponse]:
        return to_async(super().get_document_template_annotations)(
            template_id, document_id, request_config=request_config
        )

    def add_template_annotation(
        self,
        request_body: AddAnnotationRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Annotation]:
        return to_async(super().add_template_annotation)(
            request_body, template_id, request_config=request_config
        )

    def delete_template_annotation(
        self,
        template_id: str,
        annotation_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[None]:
        return to_async(super().delete_template_annotation)(
            template_id, annotation_id, request_config=request_config
        )

    def set_template_attachments_settings(
        self,
        request_body: SetEnvelopeAttachmentsSettingsRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[EnvelopeAttachments]:
        return to_async(super().set_template_attachments_settings)(
            request_body, template_id, request_config=request_config
        )

    def set_template_attachments_placeholders(
        self,
        request_body: SetEnvelopeAttachmentsPlaceholdersRequest,
        template_id: str,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[EnvelopeAttachments]:
        return to_async(super().set_template_attachments_placeholders)(
            request_body, template_id, request_config=request_config
        )

    def create_webhook(
        self,
        request_body: CreateWebhookRequest,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[Webhook]:
        return to_async(super().create_webhook)(
            request_body, request_config=request_config
        )

    def list_webhooks(
        self,
        request_body: ListWebhooksRequest = None,
        *,
        request_config: Optional[SdkConfig] = None,
    ) -> Awaitable[ListWebhooksResponse]:
        return to_async(super().list_webhooks)(
            request_body, request_config=request_config
        )

    def delete_webhook(
        self, webhook_id: str, *, request_config: Optional[SdkConfig] = None
    ) -> Awaitable[None]:
        return to_async(super().delete_webhook)(
            webhook_id, request_config=request_config
        )
