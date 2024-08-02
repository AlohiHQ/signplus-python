# Envelope

**Properties**

| Name           | Type                  | Required | Description                                                                                                                                                             |
| :------------- | :-------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_           | str                   | ❌       | Unique identifier of the envelope                                                                                                                                       |
| name           | str                   | ❌       | Name of the envelope                                                                                                                                                    |
| comment        | str                   | ❌       | Comment for the envelope                                                                                                                                                |
| pages          | int                   | ❌       | Total number of pages in the envelope                                                                                                                                   |
| flow_type      | EnvelopeFlowType      | ❌       | Flow type of the envelope (REQUEST_SIGNATURE is a request for signature, SIGN_MYSELF is a self-signing flow)                                                            |
| legality_level | EnvelopeLegalityLevel | ❌       | Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes) |
| status         | EnvelopeStatus        | ❌       | Status of the envelope                                                                                                                                                  |
| created_at     | int                   | ❌       | Unix timestamp of the creation date                                                                                                                                     |
| updated_at     | int                   | ❌       | Unix timestamp of the last modification date                                                                                                                            |
| expires_at     | int                   | ❌       | Unix timestamp of the expiration date                                                                                                                                   |
| num_recipients | int                   | ❌       | Number of recipients in the envelope                                                                                                                                    |
| is_duplicable  | bool                  | ❌       | Whether the envelope can be duplicated                                                                                                                                  |
| signing_steps  | List[SigningStep]     | ❌       |                                                                                                                                                                         |
| documents      | List[Document]        | ❌       |                                                                                                                                                                         |
| notification   | EnvelopeNotification  | ❌       |                                                                                                                                                                         |
