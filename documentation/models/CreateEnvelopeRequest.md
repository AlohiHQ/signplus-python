# CreateEnvelopeRequest

**Properties**

| Name           | Type                  | Required | Description                                                                                                                                                             |
| :------------- | :-------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name           | str                   | ✅       | Name of the envelope                                                                                                                                                    |
| flow_type      | EnvelopeFlowType      | ✅       | Flow type of the envelope (REQUEST_SIGNATURE is a request for signature, SIGN_MYSELF is a self-signing flow)                                                            |
| legality_level | EnvelopeLegalityLevel | ✅       | Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes) |
| expires_at     | int                   | ❌       | Unix timestamp of the expiration date                                                                                                                                   |
| comment        | str                   | ❌       | Comment for the envelope                                                                                                                                                |
| sandbox        | bool                  | ❌       | Whether the envelope is created in sandbox mode                                                                                                                         |
