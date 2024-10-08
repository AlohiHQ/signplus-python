from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .envelope_flow_type import EnvelopeFlowType
from .envelope_legality_level import EnvelopeLegalityLevel
from .envelope_status import EnvelopeStatus
from .signing_step import SigningStep
from .document import Document
from .envelope_notification import EnvelopeNotification


@JsonMap({"id_": "id"})
class Envelope(BaseModel):
    """Envelope

    :param id_: Unique identifier of the envelope, defaults to None
    :type id_: str, optional
    :param name: Name of the envelope, defaults to None
    :type name: str, optional
    :param comment: Comment for the envelope, defaults to None
    :type comment: str, optional
    :param pages: Total number of pages in the envelope, defaults to None
    :type pages: int, optional
    :param flow_type: Flow type of the envelope (REQUEST_SIGNATURE is a request for signature, SIGN_MYSELF is a self-signing flow), defaults to None
    :type flow_type: EnvelopeFlowType, optional
    :param legality_level: Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes), defaults to None
    :type legality_level: EnvelopeLegalityLevel, optional
    :param status: Status of the envelope, defaults to None
    :type status: EnvelopeStatus, optional
    :param created_at: Unix timestamp of the creation date, defaults to None
    :type created_at: int, optional
    :param updated_at: Unix timestamp of the last modification date, defaults to None
    :type updated_at: int, optional
    :param expires_at: Unix timestamp of the expiration date, defaults to None
    :type expires_at: int, optional
    :param num_recipients: Number of recipients in the envelope, defaults to None
    :type num_recipients: int, optional
    :param is_duplicable: Whether the envelope can be duplicated, defaults to None
    :type is_duplicable: bool, optional
    :param signing_steps: signing_steps, defaults to None
    :type signing_steps: List[SigningStep], optional
    :param documents: documents, defaults to None
    :type documents: List[Document], optional
    :param notification: notification, defaults to None
    :type notification: EnvelopeNotification, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        comment: str = None,
        pages: int = None,
        flow_type: EnvelopeFlowType = None,
        legality_level: EnvelopeLegalityLevel = None,
        status: EnvelopeStatus = None,
        created_at: int = None,
        updated_at: int = None,
        expires_at: int = None,
        num_recipients: int = None,
        is_duplicable: bool = None,
        signing_steps: List[SigningStep] = None,
        documents: List[Document] = None,
        notification: EnvelopeNotification = None,
    ):
        """Envelope

        :param id_: Unique identifier of the envelope, defaults to None
        :type id_: str, optional
        :param name: Name of the envelope, defaults to None
        :type name: str, optional
        :param comment: Comment for the envelope, defaults to None
        :type comment: str, optional
        :param pages: Total number of pages in the envelope, defaults to None
        :type pages: int, optional
        :param flow_type: Flow type of the envelope (REQUEST_SIGNATURE is a request for signature, SIGN_MYSELF is a self-signing flow), defaults to None
        :type flow_type: EnvelopeFlowType, optional
        :param legality_level: Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes), defaults to None
        :type legality_level: EnvelopeLegalityLevel, optional
        :param status: Status of the envelope, defaults to None
        :type status: EnvelopeStatus, optional
        :param created_at: Unix timestamp of the creation date, defaults to None
        :type created_at: int, optional
        :param updated_at: Unix timestamp of the last modification date, defaults to None
        :type updated_at: int, optional
        :param expires_at: Unix timestamp of the expiration date, defaults to None
        :type expires_at: int, optional
        :param num_recipients: Number of recipients in the envelope, defaults to None
        :type num_recipients: int, optional
        :param is_duplicable: Whether the envelope can be duplicated, defaults to None
        :type is_duplicable: bool, optional
        :param signing_steps: signing_steps, defaults to None
        :type signing_steps: List[SigningStep], optional
        :param documents: documents, defaults to None
        :type documents: List[Document], optional
        :param notification: notification, defaults to None
        :type notification: EnvelopeNotification, optional
        """
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if comment is not None:
            self.comment = comment
        if pages is not None:
            self.pages = pages
        if flow_type is not None:
            self.flow_type = self._enum_matching(
                flow_type, EnvelopeFlowType.list(), "flow_type"
            )
        if legality_level is not None:
            self.legality_level = self._enum_matching(
                legality_level, EnvelopeLegalityLevel.list(), "legality_level"
            )
        if status is not None:
            self.status = self._enum_matching(status, EnvelopeStatus.list(), "status")
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if expires_at is not None:
            self.expires_at = expires_at
        if num_recipients is not None:
            self.num_recipients = num_recipients
        if is_duplicable is not None:
            self.is_duplicable = is_duplicable
        if signing_steps is not None:
            self.signing_steps = self._define_list(signing_steps, SigningStep)
        if documents is not None:
            self.documents = self._define_list(documents, Document)
        if notification is not None:
            self.notification = self._define_object(notification, EnvelopeNotification)
