# RenameService

A list of all methods in the `RenameService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description     |
| :---------------------------------- | :-------------- |
| [rename_envelope](#rename_envelope) | Rename envelope |

## rename_envelope

Rename envelope

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/rename`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [RenameEnvelopeRequest](../models/RenameEnvelopeRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                         | ✅       |                   |
| accept       | str                                                         | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import RenameEnvelopeRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = RenameEnvelopeRequest(
    name="<string>"
)

result = sdk.rename.rename_envelope(
    request_body=request_body,
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
