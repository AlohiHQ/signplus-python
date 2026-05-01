# DocumentIdService

A list of all methods in the `DocumentIdService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description           |
| :---------------------------------------------- | :-------------------- |
| [get_envelope_document](#get_envelope_document) | Get envelope document |

## get_envelope_document

Get envelope document

- HTTP Method: `GET`
- Endpoint: `/envelope/{envelope_id}/document/{document_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |
| document_id | str  | ✅       |             |
| accept      | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.document_id.get_envelope_document(
    envelope_id="envelope_id",
    document_id="document_id",
    accept="application/json"
)

print(result)
```
