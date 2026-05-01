from typing import Union
from .services.template_id import TemplateIdService
from .services.signed_documents import SignedDocumentsService
from .services.certificate import CertificateService
from .services.document_id import DocumentIdService
from .services.document import DocumentService
from .services.documents import DocumentsService
from .services.dynamic_fields import DynamicFieldsService
from .services.signing_steps import SigningStepsService
from .services.settings import SettingsService
from .services.placeholders import PlaceholdersService
from .services.file_id import FileIdService
from .services.send import SendService
from .services.duplicate import DuplicateService
from .services.void import VoidService
from .services.rename import RenameService
from .services.set_comment import SetCommentService
from .services.set_notification import SetNotificationService
from .services.set_expiration_date import SetExpirationDateService
from .services.set_legality_level import SetLegalityLevelService
from .services.envelope_envelope_id_annotations_document_id import (
    EnvelopeEnvelopeIdAnnotationsDocumentIdService,
)
from .services.annotations import AnnotationsService
from .services.annotation_id import AnnotationIdService
from .services.annotation import AnnotationService
from .services.envelope_id import EnvelopeIdService
from .services.envelope import EnvelopeService
from .services.envelopes import EnvelopesService
from .services.template_template_id_duplicate import TemplateTemplateIdDuplicateService
from .services.template_template_id_document_document_id import (
    TemplateTemplateIdDocumentDocumentIdService,
)
from .services.template_template_id_document import TemplateTemplateIdDocumentService
from .services.template_template_id_documents import TemplateTemplateIdDocumentsService
from .services.template_template_id_signing_steps import (
    TemplateTemplateIdSigningStepsService,
)
from .services.template_template_id_rename import TemplateTemplateIdRenameService
from .services.template_template_id_set_comment import (
    TemplateTemplateIdSetCommentService,
)
from .services.template_template_id_set_notification import (
    TemplateTemplateIdSetNotificationService,
)
from .services.template_template_id_annotations_document_id import (
    TemplateTemplateIdAnnotationsDocumentIdService,
)
from .services.template_template_id_annotations import (
    TemplateTemplateIdAnnotationsService,
)
from .services.template_template_id_annotation_annotation_id import (
    TemplateTemplateIdAnnotationAnnotationIdService,
)
from .services.template_template_id_annotation import (
    TemplateTemplateIdAnnotationService,
)
from .services.template_template_id_attachments_settings import (
    TemplateTemplateIdAttachmentsSettingsService,
)
from .services.template_template_id_attachments_placeholders import (
    TemplateTemplateIdAttachmentsPlaceholdersService,
)
from .services.template_template_id import TemplateTemplateIdService
from .services.template import TemplateService
from .services.templates import TemplatesService
from .services.webhook_id import WebhookIdService
from .services.webhook import WebhookService
from .services.webhooks import WebhooksService
from .net.environment import Environment


class Signplus:
    """
    Main SDK client class for Signplus.
    Provides centralized configuration and access to all service endpoints.
    Supports authentication, environment management, and global timeout settings.
    """

    def __init__(
        self,
        access_token: str = None,
        base_url: Union[Environment, str, None] = None,
        timeout: int = 60000,
    ):
        """
        Initializes Signplus the SDK class.
        """

        _resolved_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )
        self._base_url = _resolved_url.rstrip("/") if _resolved_url else _resolved_url
        self.template_id = TemplateIdService(base_url=self._base_url)
        self.signed_documents = SignedDocumentsService(base_url=self._base_url)
        self.certificate = CertificateService(base_url=self._base_url)
        self.document_id = DocumentIdService(base_url=self._base_url)
        self.document = DocumentService(base_url=self._base_url)
        self.documents = DocumentsService(base_url=self._base_url)
        self.dynamic_fields = DynamicFieldsService(base_url=self._base_url)
        self.signing_steps = SigningStepsService(base_url=self._base_url)
        self.settings = SettingsService(base_url=self._base_url)
        self.placeholders = PlaceholdersService(base_url=self._base_url)
        self.file_id = FileIdService(base_url=self._base_url)
        self.send = SendService(base_url=self._base_url)
        self.duplicate = DuplicateService(base_url=self._base_url)
        self.void = VoidService(base_url=self._base_url)
        self.rename = RenameService(base_url=self._base_url)
        self.set_comment = SetCommentService(base_url=self._base_url)
        self.set_notification = SetNotificationService(base_url=self._base_url)
        self.set_expiration_date = SetExpirationDateService(base_url=self._base_url)
        self.set_legality_level = SetLegalityLevelService(base_url=self._base_url)
        self.envelope_envelope_id_annotations_document_id = (
            EnvelopeEnvelopeIdAnnotationsDocumentIdService(base_url=self._base_url)
        )
        self.annotations = AnnotationsService(base_url=self._base_url)
        self.annotation_id = AnnotationIdService(base_url=self._base_url)
        self.annotation = AnnotationService(base_url=self._base_url)
        self.envelope_id = EnvelopeIdService(base_url=self._base_url)
        self.envelope = EnvelopeService(base_url=self._base_url)
        self.envelopes = EnvelopesService(base_url=self._base_url)
        self.template_template_id_duplicate = TemplateTemplateIdDuplicateService(
            base_url=self._base_url
        )
        self.template_template_id_document_document_id = (
            TemplateTemplateIdDocumentDocumentIdService(base_url=self._base_url)
        )
        self.template_template_id_document = TemplateTemplateIdDocumentService(
            base_url=self._base_url
        )
        self.template_template_id_documents = TemplateTemplateIdDocumentsService(
            base_url=self._base_url
        )
        self.template_template_id_signing_steps = TemplateTemplateIdSigningStepsService(
            base_url=self._base_url
        )
        self.template_template_id_rename = TemplateTemplateIdRenameService(
            base_url=self._base_url
        )
        self.template_template_id_set_comment = TemplateTemplateIdSetCommentService(
            base_url=self._base_url
        )
        self.template_template_id_set_notification = (
            TemplateTemplateIdSetNotificationService(base_url=self._base_url)
        )
        self.template_template_id_annotations_document_id = (
            TemplateTemplateIdAnnotationsDocumentIdService(base_url=self._base_url)
        )
        self.template_template_id_annotations = TemplateTemplateIdAnnotationsService(
            base_url=self._base_url
        )
        self.template_template_id_annotation_annotation_id = (
            TemplateTemplateIdAnnotationAnnotationIdService(base_url=self._base_url)
        )
        self.template_template_id_annotation = TemplateTemplateIdAnnotationService(
            base_url=self._base_url
        )
        self.template_template_id_attachments_settings = (
            TemplateTemplateIdAttachmentsSettingsService(base_url=self._base_url)
        )
        self.template_template_id_attachments_placeholders = (
            TemplateTemplateIdAttachmentsPlaceholdersService(base_url=self._base_url)
        )
        self.template_template_id = TemplateTemplateIdService(base_url=self._base_url)
        self.template = TemplateService(base_url=self._base_url)
        self.templates = TemplatesService(base_url=self._base_url)
        self.webhook_id = WebhookIdService(base_url=self._base_url)
        self.webhook = WebhookService(base_url=self._base_url)
        self.webhooks = WebhooksService(base_url=self._base_url)
        self.set_access_token(access_token)
        self.set_timeout(timeout)

    def set_base_url(self, base_url: Union[Environment, str]):
        """
        Sets the base URL for the entire SDK.

        :param Union[Environment, str] base_url: The base URL to be set.
        :return: The SDK instance.
        """
        _resolved_url = (
            base_url.value if isinstance(base_url, Environment) else base_url
        )
        self._base_url = _resolved_url.rstrip("/") if _resolved_url else _resolved_url

        self.template_id.set_base_url(self._base_url)
        self.signed_documents.set_base_url(self._base_url)
        self.certificate.set_base_url(self._base_url)
        self.document_id.set_base_url(self._base_url)
        self.document.set_base_url(self._base_url)
        self.documents.set_base_url(self._base_url)
        self.dynamic_fields.set_base_url(self._base_url)
        self.signing_steps.set_base_url(self._base_url)
        self.settings.set_base_url(self._base_url)
        self.placeholders.set_base_url(self._base_url)
        self.file_id.set_base_url(self._base_url)
        self.send.set_base_url(self._base_url)
        self.duplicate.set_base_url(self._base_url)
        self.void.set_base_url(self._base_url)
        self.rename.set_base_url(self._base_url)
        self.set_comment.set_base_url(self._base_url)
        self.set_notification.set_base_url(self._base_url)
        self.set_expiration_date.set_base_url(self._base_url)
        self.set_legality_level.set_base_url(self._base_url)
        self.envelope_envelope_id_annotations_document_id.set_base_url(self._base_url)
        self.annotations.set_base_url(self._base_url)
        self.annotation_id.set_base_url(self._base_url)
        self.annotation.set_base_url(self._base_url)
        self.envelope_id.set_base_url(self._base_url)
        self.envelope.set_base_url(self._base_url)
        self.envelopes.set_base_url(self._base_url)
        self.template_template_id_duplicate.set_base_url(self._base_url)
        self.template_template_id_document_document_id.set_base_url(self._base_url)
        self.template_template_id_document.set_base_url(self._base_url)
        self.template_template_id_documents.set_base_url(self._base_url)
        self.template_template_id_signing_steps.set_base_url(self._base_url)
        self.template_template_id_rename.set_base_url(self._base_url)
        self.template_template_id_set_comment.set_base_url(self._base_url)
        self.template_template_id_set_notification.set_base_url(self._base_url)
        self.template_template_id_annotations_document_id.set_base_url(self._base_url)
        self.template_template_id_annotations.set_base_url(self._base_url)
        self.template_template_id_annotation_annotation_id.set_base_url(self._base_url)
        self.template_template_id_annotation.set_base_url(self._base_url)
        self.template_template_id_attachments_settings.set_base_url(self._base_url)
        self.template_template_id_attachments_placeholders.set_base_url(self._base_url)
        self.template_template_id.set_base_url(self._base_url)
        self.template.set_base_url(self._base_url)
        self.templates.set_base_url(self._base_url)
        self.webhook_id.set_base_url(self._base_url)
        self.webhook.set_base_url(self._base_url)
        self.webhooks.set_base_url(self._base_url)

        return self

    def set_access_token(self, access_token: str):
        """
        Sets the access token for the entire SDK.
        """
        self.template_id.set_access_token(access_token)
        self.signed_documents.set_access_token(access_token)
        self.certificate.set_access_token(access_token)
        self.document_id.set_access_token(access_token)
        self.document.set_access_token(access_token)
        self.documents.set_access_token(access_token)
        self.dynamic_fields.set_access_token(access_token)
        self.signing_steps.set_access_token(access_token)
        self.settings.set_access_token(access_token)
        self.placeholders.set_access_token(access_token)
        self.file_id.set_access_token(access_token)
        self.send.set_access_token(access_token)
        self.duplicate.set_access_token(access_token)
        self.void.set_access_token(access_token)
        self.rename.set_access_token(access_token)
        self.set_comment.set_access_token(access_token)
        self.set_notification.set_access_token(access_token)
        self.set_expiration_date.set_access_token(access_token)
        self.set_legality_level.set_access_token(access_token)
        self.envelope_envelope_id_annotations_document_id.set_access_token(access_token)
        self.annotations.set_access_token(access_token)
        self.annotation_id.set_access_token(access_token)
        self.annotation.set_access_token(access_token)
        self.envelope_id.set_access_token(access_token)
        self.envelope.set_access_token(access_token)
        self.envelopes.set_access_token(access_token)
        self.template_template_id_duplicate.set_access_token(access_token)
        self.template_template_id_document_document_id.set_access_token(access_token)
        self.template_template_id_document.set_access_token(access_token)
        self.template_template_id_documents.set_access_token(access_token)
        self.template_template_id_signing_steps.set_access_token(access_token)
        self.template_template_id_rename.set_access_token(access_token)
        self.template_template_id_set_comment.set_access_token(access_token)
        self.template_template_id_set_notification.set_access_token(access_token)
        self.template_template_id_annotations_document_id.set_access_token(access_token)
        self.template_template_id_annotations.set_access_token(access_token)
        self.template_template_id_annotation_annotation_id.set_access_token(
            access_token
        )
        self.template_template_id_annotation.set_access_token(access_token)
        self.template_template_id_attachments_settings.set_access_token(access_token)
        self.template_template_id_attachments_placeholders.set_access_token(
            access_token
        )
        self.template_template_id.set_access_token(access_token)
        self.template.set_access_token(access_token)
        self.templates.set_access_token(access_token)
        self.webhook_id.set_access_token(access_token)
        self.webhook.set_access_token(access_token)
        self.webhooks.set_access_token(access_token)

        return self

    def set_timeout(self, timeout: int):
        """
        Sets the timeout for the entire SDK.

        :param int timeout: The timeout (ms) to be set.
        :return: The SDK instance.
        """
        self.template_id.set_timeout(timeout)
        self.signed_documents.set_timeout(timeout)
        self.certificate.set_timeout(timeout)
        self.document_id.set_timeout(timeout)
        self.document.set_timeout(timeout)
        self.documents.set_timeout(timeout)
        self.dynamic_fields.set_timeout(timeout)
        self.signing_steps.set_timeout(timeout)
        self.settings.set_timeout(timeout)
        self.placeholders.set_timeout(timeout)
        self.file_id.set_timeout(timeout)
        self.send.set_timeout(timeout)
        self.duplicate.set_timeout(timeout)
        self.void.set_timeout(timeout)
        self.rename.set_timeout(timeout)
        self.set_comment.set_timeout(timeout)
        self.set_notification.set_timeout(timeout)
        self.set_expiration_date.set_timeout(timeout)
        self.set_legality_level.set_timeout(timeout)
        self.envelope_envelope_id_annotations_document_id.set_timeout(timeout)
        self.annotations.set_timeout(timeout)
        self.annotation_id.set_timeout(timeout)
        self.annotation.set_timeout(timeout)
        self.envelope_id.set_timeout(timeout)
        self.envelope.set_timeout(timeout)
        self.envelopes.set_timeout(timeout)
        self.template_template_id_duplicate.set_timeout(timeout)
        self.template_template_id_document_document_id.set_timeout(timeout)
        self.template_template_id_document.set_timeout(timeout)
        self.template_template_id_documents.set_timeout(timeout)
        self.template_template_id_signing_steps.set_timeout(timeout)
        self.template_template_id_rename.set_timeout(timeout)
        self.template_template_id_set_comment.set_timeout(timeout)
        self.template_template_id_set_notification.set_timeout(timeout)
        self.template_template_id_annotations_document_id.set_timeout(timeout)
        self.template_template_id_annotations.set_timeout(timeout)
        self.template_template_id_annotation_annotation_id.set_timeout(timeout)
        self.template_template_id_annotation.set_timeout(timeout)
        self.template_template_id_attachments_settings.set_timeout(timeout)
        self.template_template_id_attachments_placeholders.set_timeout(timeout)
        self.template_template_id.set_timeout(timeout)
        self.template.set_timeout(timeout)
        self.templates.set_timeout(timeout)
        self.webhook_id.set_timeout(timeout)
        self.webhook.set_timeout(timeout)
        self.webhooks.set_timeout(timeout)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
