# TemplateTemplateIdAttachmentsPlaceholdersService

A list of all methods in the `TemplateTemplateIdAttachmentsPlaceholdersService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                                                     |
| :------------------------------------------------------------------------------ | :-------------------------------------------------------------- |
| [set_template_attachments_placeholders](#set_template_attachments_placeholders) | Placeholders to be set, completely replacing the existing ones. |

## set_template_attachments_placeholders

Placeholders to be set, completely replacing the existing ones.

- HTTP Method: `PUT`
- Endpoint: `/template/{template_id}/attachments/placeholders`

**Parameters**

| Name         | Type                                                                                                | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [SetTemplateAttachmentsPlaceholdersRequest](../models/SetTemplateAttachmentsPlaceholdersRequest.md) | ✅       | The request body. |
| template_id  | str                                                                                                 | ✅       |                   |
| accept       | str                                                                                                 | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetTemplateAttachmentsPlaceholdersRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetTemplateAttachmentsPlaceholdersRequest(
    placeholders=[
        {
            "recipient_id": "string",
            "name": "string",
            "required": False,
            "multiple": False,
            "id_": "string",
            "hint": "string"
        }
    ]
)

result = sdk.template_template_id_attachments_placeholders.set_template_attachments_placeholders(
    request_body=request_body,
    template_id="template_id",
    accept="application/json"
)

print(result)
```
