"""Lazy model exports.

Names are resolved on first attribute access via PEP 562 ``__getattr__``,
then cached in module globals. Avoids the multi-second eager-import cost
on SDKs with thousands of generated models.
"""

import importlib

_MODEL_TO_MODULE = {
    "CreateEnvelopeRequest": "create_envelope_request",
    "Envelope": "envelope",
    "CreateEnvelopeFromTemplateRequest": "create_envelope_from_template_request",
    "ListEnvelopesRequest": "list_envelopes_request",
    "ListEnvelopesResponse": "list_envelopes_response",
    "Document": "document",
    "ListEnvelopeDocumentsResponse": "list_envelope_documents_response",
    "AddEnvelopeDocumentRequest": "add_envelope_document_request",
    "SetEnvelopeDynamicFieldsRequest": "set_envelope_dynamic_fields_request",
    "AddEnvelopeSigningStepsRequest": "add_envelope_signing_steps_request",
    "SetEnvelopeAttachmentsSettingsRequest": "set_envelope_attachments_settings_request",
    "EnvelopeAttachments": "envelope_attachments",
    "SetEnvelopeAttachmentsPlaceholdersRequest": "set_envelope_attachments_placeholders_request",
    "RenameEnvelopeRequest": "rename_envelope_request",
    "SetEnvelopeCommentRequest": "set_envelope_comment_request",
    "EnvelopeNotification": "envelope_notification",
    "SetEnvelopeExpirationRequest": "set_envelope_expiration_request",
    "SetEnvelopeLegalityLevelRequest": "set_envelope_legality_level_request",
    "Annotation": "annotation",
    "ListEnvelopeDocumentAnnotationsResponse": "list_envelope_document_annotations_response",
    "AddAnnotationRequest": "add_annotation_request",
    "CreateTemplateRequest": "create_template_request",
    "Template": "template",
    "ListTemplatesRequest": "list_templates_request",
    "ListTemplatesResponse": "list_templates_response",
    "AddTemplateDocumentRequest": "add_template_document_request",
    "ListTemplateDocumentsResponse": "list_template_documents_response",
    "AddTemplateSigningStepsRequest": "add_template_signing_steps_request",
    "RenameTemplateRequest": "rename_template_request",
    "SetTemplateCommentRequest": "set_template_comment_request",
    "ListTemplateAnnotationsResponse": "list_template_annotations_response",
    "ListTemplateDocumentAnnotationsResponse": "list_template_document_annotations_response",
    "CreateWebhookRequest": "create_webhook_request",
    "Webhook": "webhook",
    "ListWebhooksRequest": "list_webhooks_request",
    "ListWebhooksResponse": "list_webhooks_response",
    "EnvelopeLegalityLevel": "envelope_legality_level",
    "EnvelopeFlowType": "envelope_flow_type",
    "EnvelopeStatus": "envelope_status",
    "SigningStep": "signing_step",
    "Recipient": "recipient",
    "RecipientRole": "recipient_role",
    "RecipientVerification": "recipient_verification",
    "RecipientVerificationType": "recipient_verification_type",
    "Page": "page",
    "AttachmentSettings": "attachment_settings",
    "AttachmentPlaceholdersPerRecipient": "attachment_placeholders_per_recipient",
    "AttachmentPlaceholder": "attachment_placeholder",
    "AttachmentPlaceholderFile": "attachment_placeholder_file",
    "EnvelopeOrderField": "envelope_order_field",
    "DynamicField": "dynamic_field",
    "AttachmentPlaceholderRequest": "attachment_placeholder_request",
    "AnnotationType": "annotation_type",
    "AnnotationSignature": "annotation_signature",
    "AnnotationInitials": "annotation_initials",
    "AnnotationText": "annotation_text",
    "AnnotationDateTime": "annotation_date_time",
    "AnnotationCheckbox": "annotation_checkbox",
    "AnnotationFont": "annotation_font",
    "AnnotationFontFamily": "annotation_font_family",
    "AnnotationDateTimeFormat": "annotation_date_time_format",
    "AnnotationCheckboxStyle": "annotation_checkbox_style",
    "TemplateSigningStep": "template_signing_step",
    "TemplateRecipient": "template_recipient",
    "TemplateRecipientRole": "template_recipient_role",
    "TemplateOrderField": "template_order_field",
    "WebhookEvent": "webhook_event",
}

_REBUILD_NAMES = frozenset(
    {
        "CreateEnvelopeRequest",
        "Envelope",
        "CreateEnvelopeFromTemplateRequest",
        "ListEnvelopesRequest",
        "ListEnvelopesResponse",
        "Document",
        "ListEnvelopeDocumentsResponse",
        "AddEnvelopeDocumentRequest",
        "SetEnvelopeDynamicFieldsRequest",
        "AddEnvelopeSigningStepsRequest",
        "SetEnvelopeAttachmentsSettingsRequest",
        "EnvelopeAttachments",
        "SetEnvelopeAttachmentsPlaceholdersRequest",
        "RenameEnvelopeRequest",
        "SetEnvelopeCommentRequest",
        "EnvelopeNotification",
        "SetEnvelopeExpirationRequest",
        "SetEnvelopeLegalityLevelRequest",
        "Annotation",
        "ListEnvelopeDocumentAnnotationsResponse",
        "AddAnnotationRequest",
        "CreateTemplateRequest",
        "Template",
        "ListTemplatesRequest",
        "ListTemplatesResponse",
        "AddTemplateDocumentRequest",
        "ListTemplateDocumentsResponse",
        "AddTemplateSigningStepsRequest",
        "RenameTemplateRequest",
        "SetTemplateCommentRequest",
        "ListTemplateAnnotationsResponse",
        "ListTemplateDocumentAnnotationsResponse",
        "CreateWebhookRequest",
        "Webhook",
        "ListWebhooksRequest",
        "ListWebhooksResponse",
        "SigningStep",
        "Recipient",
        "RecipientVerification",
        "Page",
        "AttachmentSettings",
        "AttachmentPlaceholdersPerRecipient",
        "AttachmentPlaceholder",
        "AttachmentPlaceholderFile",
        "DynamicField",
        "AttachmentPlaceholderRequest",
        "AnnotationSignature",
        "AnnotationInitials",
        "AnnotationText",
        "AnnotationDateTime",
        "AnnotationCheckbox",
        "AnnotationFont",
        "TemplateSigningStep",
        "TemplateRecipient",
    }
)

__all__ = list(_MODEL_TO_MODULE.keys())

_rebuilt = False


def _load(name):
    module = _MODEL_TO_MODULE.get(name)
    if module is None:
        return None
    obj = getattr(importlib.import_module("." + module, __name__), name)
    globals()[name] = obj
    return obj


def _ensure_rebuilt():
    """Resolve forward refs across every BaseModel in one batched pass.

    Individual model files import their cross-references inside a
    ``TYPE_CHECKING`` block, so at runtime each file's globals contain
    only itself. ``model_rebuild()`` walks the call stack to find
    forward-ref names — calling it from this module once every
    BaseModel has been loaded into our globals is what lets pydantic
    resolve circular refs (the same shape the prior eager-import form
    relied on). Enums, Union types, and error models stay lazy.
    """
    global _rebuilt
    if _rebuilt:
        return
    _rebuilt = True
    for name in _REBUILD_NAMES:
        if name not in globals():
            try:
                _load(name)
            except Exception:
                pass
    ns = globals()
    for name in _REBUILD_NAMES:
        cls = ns.get(name)
        if cls is None:
            continue
        try:
            # _types_namespace is mandatory: pydantic resolves forward refs
            # against caller-frame locals by default, but we're calling from
            # inside a helper — the names live in this module's globals.
            cls.model_rebuild(_types_namespace=ns)
        except Exception:
            pass


def __getattr__(name):
    if name not in _MODEL_TO_MODULE:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    obj = _load(name)
    if name in _REBUILD_NAMES:
        _ensure_rebuilt()
    return obj


def __dir__():
    return sorted(set(globals()).union(_MODEL_TO_MODULE))
