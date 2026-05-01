# DocumentService

A list of all methods in the `DocumentService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description           |
| :---------------------------------------------- | :-------------------- |
| [add_envelope_document](#add_envelope_document) | Add envelope document |

## add_envelope_document

Add envelope document

- HTTP Method: `POST`
- Endpoint: `/envelope/{envelope_id}/document`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AddEnvelopeDocumentRequest](../models/AddEnvelopeDocumentRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                   | ✅       |                   |
| accept       | str                                                                   | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import AddEnvelopeDocumentRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AddEnvelopeDocumentRequest(
    file=""
)

result = sdk.document.add_envelope_document(
    request_body=request_body,
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
