# TemplateTemplateIdDuplicateService

A list of all methods in the `TemplateTemplateIdDuplicateService` service. Click on the method name to view detailed information about that method.

| Methods                                   | Description        |
| :---------------------------------------- | :----------------- |
| [duplicate_template](#duplicate_template) | Duplicate template |

## duplicate_template

Duplicate template

- HTTP Method: `POST`
- Endpoint: `/template/{template_id}/duplicate`

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

result = sdk.template_template_id_duplicate.duplicate_template(
    template_id="template_id",
    accept="application/json"
)

print(result)
```
