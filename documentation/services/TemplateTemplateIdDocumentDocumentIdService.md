# TemplateTemplateIdDocumentDocumentIdService

A list of all methods in the `TemplateTemplateIdDocumentDocumentIdService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description           |
| :---------------------------------------------- | :-------------------- |
| [get_template_document](#get_template_document) | Get template document |

## get_template_document

Get template document

- HTTP Method: `GET`
- Endpoint: `/template/{template_id}/document/{document_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| template_id | str  | ✅       |             |
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

result = sdk.template_template_id_document_document_id.get_template_document(
    template_id="template_id",
    document_id="document_id",
    accept="application/json"
)

print(result)
```
