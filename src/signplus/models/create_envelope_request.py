from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .envelope_flow_type import EnvelopeFlowType
from .envelope_legality_level import EnvelopeLegalityLevel


@JsonMap({})
class CreateEnvelopeRequest(BaseModel):
    """CreateEnvelopeRequest

    :param name: Name of the envelope, defaults to None
    :type name: str, optional
    :param flow_type: Flow type of the envelope (REQUEST_SIGNATURE is a request for signature, SIGN_MYSELF is a self-signing flow), defaults to None
    :type flow_type: EnvelopeFlowType, optional
    :param legality_level: Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes), defaults to None
    :type legality_level: EnvelopeLegalityLevel, optional
    :param expires_at: Unix timestamp of the expiration date, defaults to None
    :type expires_at: int, optional
    :param comment: Comment for the envelope, defaults to None
    :type comment: str, optional
    :param sandbox: Whether the envelope is created in sandbox mode, defaults to None
    :type sandbox: bool, optional
    """

    def __init__(
        self,
        name: str = None,
        flow_type: EnvelopeFlowType = None,
        legality_level: EnvelopeLegalityLevel = None,
        expires_at: int = None,
        comment: str = None,
        sandbox: bool = None,
    ):
        """CreateEnvelopeRequest

        :param name: Name of the envelope, defaults to None
        :type name: str, optional
        :param flow_type: Flow type of the envelope (REQUEST_SIGNATURE is a request for signature, SIGN_MYSELF is a self-signing flow), defaults to None
        :type flow_type: EnvelopeFlowType, optional
        :param legality_level: Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes), defaults to None
        :type legality_level: EnvelopeLegalityLevel, optional
        :param expires_at: Unix timestamp of the expiration date, defaults to None
        :type expires_at: int, optional
        :param comment: Comment for the envelope, defaults to None
        :type comment: str, optional
        :param sandbox: Whether the envelope is created in sandbox mode, defaults to None
        :type sandbox: bool, optional
        """
        if name is not None:
            self.name = name
        if flow_type is not None:
            self.flow_type = self._enum_matching(
                flow_type, EnvelopeFlowType.list(), "flow_type"
            )
        if legality_level is not None:
            self.legality_level = self._enum_matching(
                legality_level, EnvelopeLegalityLevel.list(), "legality_level"
            )
        if expires_at is not None:
            self.expires_at = expires_at
        if comment is not None:
            self.comment = comment
        if sandbox is not None:
            self.sandbox = sandbox
