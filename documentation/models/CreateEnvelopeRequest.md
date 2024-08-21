# CreateEnvelopeRequest

**Properties**

| Name           | Type                  | Required | Description                                                                                                                                                             |
| :------------- | :-------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name           | str                   | ✅       | Name of the envelope                                                                                                                                                    |
| legality_level | EnvelopeLegalityLevel | ✅       | Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes) |
| expires_at     | int                   | ❌       | Unix timestamp of the expiration date                                                                                                                                   |
| comment        | str                   | ❌       | Comment for the envelope                                                                                                                                                |
| sandbox        | bool                  | ❌       | Whether the envelope is created in sandbox mode                                                                                                                         |
