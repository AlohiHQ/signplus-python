# DocumentsService

A list of all methods in the `DocumentsService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description            |
| :------------------------------------------------ | :--------------------- |
| [get_envelope_documents](#get_envelope_documents) | Get envelope documents |

## get_envelope_documents

Get envelope documents

- HTTP Method: `GET`
- Endpoint: `/envelope/{envelope_id}/documents`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |
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

result = sdk.documents.get_envelope_documents(
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
