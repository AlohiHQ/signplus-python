# PlaceholdersService

A list of all methods in the `PlaceholdersService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                                                     |
| :------------------------------------------------------------------------------ | :-------------------------------------------------------------- |
| [set_envelope_attachments_placeholders](#set_envelope_attachments_placeholders) | Placeholders to be set, completely replacing the existing ones. |

## set_envelope_attachments_placeholders

Placeholders to be set, completely replacing the existing ones.

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/attachments/placeholders`

**Parameters**

| Name         | Type                                                                                                | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [SetEnvelopeAttachmentsPlaceholdersRequest](../models/SetEnvelopeAttachmentsPlaceholdersRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                                                 | ✅       |                   |
| accept       | str                                                                                                 | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetEnvelopeAttachmentsPlaceholdersRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetEnvelopeAttachmentsPlaceholdersRequest(
    placeholders=[
        {
            "recipient_id": "string",
            "name": "string",
            "required": False,
            "multiple": False,
            "id_": "string",
            "hint": "string"
        }
    ]
)

result = sdk.placeholders.set_envelope_attachments_placeholders(
    request_body=request_body,
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
