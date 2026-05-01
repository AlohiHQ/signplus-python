# SignedDocumentsService

A list of all methods in the `SignedDocumentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                               |
| :------------------------------------------------------------------------ | :---------------------------------------- |
| [download_envelope_signed_documents](#download_envelope_signed_documents) | Download signed documents for an envelope |

## download_envelope_signed_documents

Download signed documents for an envelope

- HTTP Method: `GET`
- Endpoint: `/envelope/{envelope_id}/signed_documents`

**Parameters**

| Name                      | Type | Required | Description                                                             |
| :------------------------ | :--- | :------- | :---------------------------------------------------------------------- |
| envelope_id               | str  | ✅       |                                                                         |
| accept                    | str  | ✅       |                                                                         |
| certificate_of_completion | str  | ❌       | Whether to include the certificate of completion in the downloaded file |

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

result = sdk.signed_documents.download_envelope_signed_documents(
    envelope_id="envelope_id",
    accept="application/pdf",
    certificate_of_completion="true"
)

print(result)
```
