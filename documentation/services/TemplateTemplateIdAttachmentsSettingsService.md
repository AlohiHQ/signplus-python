# TemplateTemplateIdAttachmentsSettingsService

A list of all methods in the `TemplateTemplateIdAttachmentsSettingsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                      |
| :---------------------------------------------------------------------- | :------------------------------- |
| [set_template_attachments_settings](#set_template_attachments_settings) | Set template attachment settings |

## set_template_attachments_settings

Set template attachment settings

- HTTP Method: `PUT`
- Endpoint: `/template/{template_id}/attachments/settings`

**Parameters**

| Name         | Type                                                                                        | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SetTemplateAttachmentsSettingsRequest](../models/SetTemplateAttachmentsSettingsRequest.md) | ✅       | The request body. |
| template_id  | str                                                                                         | ✅       |                   |
| accept       | str                                                                                         | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetTemplateAttachmentsSettingsRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetTemplateAttachmentsSettingsRequest(
    settings={
        "visible_to_recipients": "<boolean>"
    }
)

result = sdk.template_template_id_attachments_settings.set_template_attachments_settings(
    request_body=request_body,
    template_id="template_id",
    accept="application/json"
)

print(result)
```
