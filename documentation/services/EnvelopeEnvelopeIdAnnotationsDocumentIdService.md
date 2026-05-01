# EnvelopeEnvelopeIdAnnotationsDocumentIdService

A list of all methods in the `EnvelopeEnvelopeIdAnnotationsDocumentIdService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                       |
| :---------------------------------------------------------------------- | :-------------------------------- |
| [get_envelope_document_annotations](#get_envelope_document_annotations) | Get envelope document annotations |

## get_envelope_document_annotations

Get envelope document annotations

- HTTP Method: `GET`
- Endpoint: `/envelope/{envelope_id}/annotations/{document_id}`

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

result = sdk.envelope_envelope_id_annotations_document_id.get_envelope_document_annotations(
    envelope_id="envelope_id",
    document_id="document_id",
    accept="application/json"
)

print(result)
```
