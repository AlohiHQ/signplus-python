# TemplateTemplateIdRenameService

A list of all methods in the `TemplateTemplateIdRenameService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description     |
| :---------------------------------- | :-------------- |
| [rename_template](#rename_template) | Rename template |

## rename_template

Rename template

- HTTP Method: `PUT`
- Endpoint: `/template/{template_id}/rename`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [RenameTemplateRequest](../models/RenameTemplateRequest.md) | ✅       | The request body. |
| template_id  | str                                                         | ✅       |                   |
| accept       | str                                                         | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import RenameTemplateRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = RenameTemplateRequest(
    name="<string>"
)

result = sdk.template_template_id_rename.rename_template(
    request_body=request_body,
    template_id="template_id",
    accept="application/json"
)

print(result)
```
