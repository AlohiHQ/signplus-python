# TemplateTemplateIdDocumentService

A list of all methods in the `TemplateTemplateIdDocumentService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description           |
| :---------------------------------------------- | :-------------------- |
| [add_template_document](#add_template_document) | Add template document |

## add_template_document

Add template document

- HTTP Method: `POST`
- Endpoint: `/template/{template_id}/document`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AddTemplateDocumentRequest](../models/AddTemplateDocumentRequest.md) | ✅       | The request body. |
| template_id  | str                                                                   | ✅       |                   |
| accept       | str                                                                   | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import AddTemplateDocumentRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AddTemplateDocumentRequest(
    file=""
)

result = sdk.template_template_id_document.add_template_document(
    request_body=request_body,
    template_id="template_id",
    accept="application/json"
)

print(result)
```
