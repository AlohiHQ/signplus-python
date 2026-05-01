# TemplateTemplateIdSetNotificationService

A list of all methods in the `TemplateTemplateIdSetNotificationService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description               |
| :------------------------------------------------------ | :------------------------ |
| [set_template_notification](#set_template_notification) | Set template notification |

## set_template_notification

Set template notification

- HTTP Method: `PUT`
- Endpoint: `/template/{template_id}/set_notification`

**Parameters**

| Name         | Type                                                                          | Required | Description       |
| :----------- | :---------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [SetTemplateNotificationRequest](../models/SetTemplateNotificationRequest.md) | ✅       | The request body. |
| template_id  | str                                                                           | ✅       |                   |
| accept       | str                                                                           | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetTemplateNotificationRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetTemplateNotificationRequest(
    subject="string",
    message="string",
    reminder_interval=4732
)

result = sdk.template_template_id_set_notification.set_template_notification(
    request_body=request_body,
    template_id="template_id",
    accept="application/json"
)

print(result)
```
