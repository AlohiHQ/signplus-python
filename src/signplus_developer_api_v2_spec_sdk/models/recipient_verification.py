from __future__ import annotations
from pydantic import Field
from typing import Optional
from .utils.base_model import BaseModel
from .recipient_verification_type import RecipientVerificationType


class RecipientVerification(BaseModel):
    """RecipientVerification

    :param type_: Type of verification the recipient must complete before accessing the envelope. - `PASSCODE`: requires a code to be entered. - `SMS`: sends a code via SMS. - `ID_VERIFICATION`: prompts the recipient to complete an automated ID and selfie check., defaults to None
    :type type_: RecipientVerificationType, optional
    :param value: Required for `PASSCODE` and `SMS` verification. - `PASSCODE`: code required by the recipient to sign the document. - `SMS`: recipient's phone number. - `ID_VERIFICATION`: leave empty., defaults to None
    :type value: str, optional
    """

    type_: Optional[RecipientVerificationType] = Field(
        alias="type",
        serialization_alias="type",
        default=None,
        description="Type of verification the recipient must complete before accessing the envelope. - `PASSCODE`: requires a code to be entered. - `SMS`: sends a code via SMS. - `ID_VERIFICATION`: prompts the recipient to complete an automated ID and selfie check.",
    )
    value: Optional[str] = Field(
        default=None,
        description="Required for `PASSCODE` and `SMS` verification. - `PASSCODE`: code required by the recipient to sign the document. - `SMS`: recipient's phone number. - `ID_VERIFICATION`: leave empty.",
    )
