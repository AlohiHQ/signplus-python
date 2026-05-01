# TemplateTemplateIdDocumentsService

A list of all methods in the `TemplateTemplateIdDocumentsService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description            |
| :------------------------------------------------ | :--------------------- |
| [get_template_documents](#get_template_documents) | Get template documents |

## get_template_documents

Get template documents

- HTTP Method: `GET`
- Endpoint: `/template/{template_id}/documents`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| template_id | str  | ✅       |             |
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

result = sdk.template_template_id_documents.get_template_documents(
    template_id="template_id",
    accept="application/json"
)

print(result)
```
