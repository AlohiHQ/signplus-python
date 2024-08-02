# Template

**Properties**

| Name             | Type                      | Required | Description                                                                                                                                                             |
| :--------------- | :------------------------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_             | str                       | ❌       | Unique identifier of the template                                                                                                                                       |
| name             | str                       | ❌       | Name of the template                                                                                                                                                    |
| comment          | str                       | ❌       | Comment for the template                                                                                                                                                |
| pages            | int                       | ❌       | Total number of pages in the template                                                                                                                                   |
| legality_level   | EnvelopeLegalityLevel     | ❌       | Legal level of the envelope (SES is Simple Electronic Signature, QES_EIDAS is Qualified Electronic Signature, QES_ZERTES is Qualified Electronic Signature with Zertes) |
| created_at       | int                       | ❌       | Unix timestamp of the creation date                                                                                                                                     |
| updated_at       | int                       | ❌       | Unix timestamp of the last modification date                                                                                                                            |
| expiration_delay | int                       | ❌       | Expiration delay added to the current time when an envelope is created from this template                                                                               |
| num_recipients   | int                       | ❌       | Number of recipients in the envelope                                                                                                                                    |
| signing_steps    | List[TemplateSigningStep] | ❌       |                                                                                                                                                                         |
| documents        | List[Document]            | ❌       |                                                                                                                                                                         |
| notification     | EnvelopeNotification      | ❌       |                                                                                                                                                                         |
| dynamic_fields   | List[str]                 | ❌       | List of dynamic fields                                                                                                                                                  |
