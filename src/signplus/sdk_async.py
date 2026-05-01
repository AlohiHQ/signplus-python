from typing import Union
from .net.environment import Environment
from .sdk import Signplus
from .services.async_.template_id import TemplateIdServiceAsync
from .services.async_.signed_documents import SignedDocumentsServiceAsync
from .services.async_.certificate import CertificateServiceAsync
from .services.async_.document_id import DocumentIdServiceAsync
from .services.async_.document import DocumentServiceAsync
from .services.async_.documents import DocumentsServiceAsync
from .services.async_.dynamic_fields import DynamicFieldsServiceAsync
from .services.async_.signing_steps import SigningStepsServiceAsync
from .services.async_.settings import SettingsServiceAsync
from .services.async_.placeholders import PlaceholdersServiceAsync
from .services.async_.file_id import FileIdServiceAsync
from .services.async_.send import SendServiceAsync
from .services.async_.duplicate import DuplicateServiceAsync
from .services.async_.void import VoidServiceAsync
from .services.async_.rename import RenameServiceAsync
from .services.async_.set_comment import SetCommentServiceAsync
from .services.async_.set_notification import SetNotificationServiceAsync
from .services.async_.set_expiration_date import SetExpirationDateServiceAsync
from .services.async_.set_legality_level import SetLegalityLevelServiceAsync
from .services.async_.envelope_envelope_id_annotations_document_id import (
    EnvelopeEnvelopeIdAnnotationsDocumentIdServiceAsync,
)
from .services.async_.annotations import AnnotationsServiceAsync
from .services.async_.annotation_id import AnnotationIdServiceAsync
from .services.async_.annotation import AnnotationServiceAsync
from .services.async_.envelope_id import EnvelopeIdServiceAsync
from .services.async_.envelope import EnvelopeServiceAsync
from .services.async_.envelopes import EnvelopesServiceAsync
from .services.async_.template_template_id_duplicate import (
    TemplateTemplateIdDuplicateServiceAsync,
)
from .services.async_.template_template_id_document_document_id import (
    TemplateTemplateIdDocumentDocumentIdServiceAsync,
)
from .services.async_.template_template_id_document import (
    TemplateTemplateIdDocumentServiceAsync,
)
from .services.async_.template_template_id_documents import (
    TemplateTemplateIdDocumentsServiceAsync,
)
from .services.async_.template_template_id_signing_steps import (
    TemplateTemplateIdSigningStepsServiceAsync,
)
from .services.async_.template_template_id_rename import (
    TemplateTemplateIdRenameServiceAsync,
)
from .services.async_.template_template_id_set_comment import (
    TemplateTemplateIdSetCommentServiceAsync,
)
from .services.async_.template_template_id_set_notification import (
    TemplateTemplateIdSetNotificationServiceAsync,
)
from .services.async_.template_template_id_annotations_document_id import (
    TemplateTemplateIdAnnotationsDocumentIdServiceAsync,
)
from .services.async_.template_template_id_annotations import (
    TemplateTemplateIdAnnotationsServiceAsync,
)
from .services.async_.template_template_id_annotation_annotation_id import (
    TemplateTemplateIdAnnotationAnnotationIdServiceAsync,
)
from .services.async_.template_template_id_annotation import (
    TemplateTemplateIdAnnotationServiceAsync,
)
from .services.async_.template_template_id_attachments_settings import (
    TemplateTemplateIdAttachmentsSettingsServiceAsync,
)
from .services.async_.template_template_id_attachments_placeholders import (
    TemplateTemplateIdAttachmentsPlaceholdersServiceAsync,
)
from .services.async_.template_template_id import TemplateTemplateIdServiceAsync
from .services.async_.template import TemplateServiceAsync
from .services.async_.templates import TemplatesServiceAsync
from .services.async_.webhook_id import WebhookIdServiceAsync
from .services.async_.webhook import WebhookServiceAsync
from .services.async_.webhooks import WebhooksServiceAsync


class SignplusAsync(Signplus):
    """
    SignplusAsync is the asynchronous version of the Signplus SDK Client.
    """

    def __init__(
        self,
        access_token: str = None,
        base_url: Union[Environment, str, None] = None,
        timeout: int = 60000,
    ):
        super().__init__(access_token=access_token, base_url=base_url, timeout=timeout)

        self.template_id = TemplateIdServiceAsync(base_url=self._base_url)
        self.signed_documents = SignedDocumentsServiceAsync(base_url=self._base_url)
        self.certificate = CertificateServiceAsync(base_url=self._base_url)
        self.document_id = DocumentIdServiceAsync(base_url=self._base_url)
        self.document = DocumentServiceAsync(base_url=self._base_url)
        self.documents = DocumentsServiceAsync(base_url=self._base_url)
        self.dynamic_fields = DynamicFieldsServiceAsync(base_url=self._base_url)
        self.signing_steps = SigningStepsServiceAsync(base_url=self._base_url)
        self.settings = SettingsServiceAsync(base_url=self._base_url)
        self.placeholders = PlaceholdersServiceAsync(base_url=self._base_url)
        self.file_id = FileIdServiceAsync(base_url=self._base_url)
        self.send = SendServiceAsync(base_url=self._base_url)
        self.duplicate = DuplicateServiceAsync(base_url=self._base_url)
        self.void = VoidServiceAsync(base_url=self._base_url)
        self.rename = RenameServiceAsync(base_url=self._base_url)
        self.set_comment = SetCommentServiceAsync(base_url=self._base_url)
        self.set_notification = SetNotificationServiceAsync(base_url=self._base_url)
        self.set_expiration_date = SetExpirationDateServiceAsync(
            base_url=self._base_url
        )
        self.set_legality_level = SetLegalityLevelServiceAsync(base_url=self._base_url)
        self.envelope_envelope_id_annotations_document_id = (
            EnvelopeEnvelopeIdAnnotationsDocumentIdServiceAsync(base_url=self._base_url)
        )
        self.annotations = AnnotationsServiceAsync(base_url=self._base_url)
        self.annotation_id = AnnotationIdServiceAsync(base_url=self._base_url)
        self.annotation = AnnotationServiceAsync(base_url=self._base_url)
        self.envelope_id = EnvelopeIdServiceAsync(base_url=self._base_url)
        self.envelope = EnvelopeServiceAsync(base_url=self._base_url)
        self.envelopes = EnvelopesServiceAsync(base_url=self._base_url)
        self.template_template_id_duplicate = TemplateTemplateIdDuplicateServiceAsync(
            base_url=self._base_url
        )
        self.template_template_id_document_document_id = (
            TemplateTemplateIdDocumentDocumentIdServiceAsync(base_url=self._base_url)
        )
        self.template_template_id_document = TemplateTemplateIdDocumentServiceAsync(
            base_url=self._base_url
        )
        self.template_template_id_documents = TemplateTemplateIdDocumentsServiceAsync(
            base_url=self._base_url
        )
        self.template_template_id_signing_steps = (
            TemplateTemplateIdSigningStepsServiceAsync(base_url=self._base_url)
        )
        self.template_template_id_rename = TemplateTemplateIdRenameServiceAsync(
            base_url=self._base_url
        )
        self.template_template_id_set_comment = (
            TemplateTemplateIdSetCommentServiceAsync(base_url=self._base_url)
        )
        self.template_template_id_set_notification = (
            TemplateTemplateIdSetNotificationServiceAsync(base_url=self._base_url)
        )
        self.template_template_id_annotations_document_id = (
            TemplateTemplateIdAnnotationsDocumentIdServiceAsync(base_url=self._base_url)
        )
        self.template_template_id_annotations = (
            TemplateTemplateIdAnnotationsServiceAsync(base_url=self._base_url)
        )
        self.template_template_id_annotation_annotation_id = (
            TemplateTemplateIdAnnotationAnnotationIdServiceAsync(
                base_url=self._base_url
            )
        )
        self.template_template_id_annotation = TemplateTemplateIdAnnotationServiceAsync(
            base_url=self._base_url
        )
        self.template_template_id_attachments_settings = (
            TemplateTemplateIdAttachmentsSettingsServiceAsync(base_url=self._base_url)
        )
        self.template_template_id_attachments_placeholders = (
            TemplateTemplateIdAttachmentsPlaceholdersServiceAsync(
                base_url=self._base_url
            )
        )
        self.template_template_id = TemplateTemplateIdServiceAsync(
            base_url=self._base_url
        )
        self.template = TemplateServiceAsync(base_url=self._base_url)
        self.templates = TemplatesServiceAsync(base_url=self._base_url)
        self.webhook_id = WebhookIdServiceAsync(base_url=self._base_url)
        self.webhook = WebhookServiceAsync(base_url=self._base_url)
        self.webhooks = WebhooksServiceAsync(base_url=self._base_url)
