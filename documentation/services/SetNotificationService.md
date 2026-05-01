# SetNotificationService

A list of all methods in the `SetNotificationService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description               |
| :------------------------------------------------------ | :------------------------ |
| [set_envelope_notification](#set_envelope_notification) | Set envelope notification |

## set_envelope_notification

Set envelope notification

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/set_notification`

**Parameters**

| Name         | Type                                                                          | Required | Description       |
| :----------- | :---------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [SetEnvelopeNotificationRequest](../models/SetEnvelopeNotificationRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                           | ✅       |                   |
| accept       | str                                                                           | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetEnvelopeNotificationRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetEnvelopeNotificationRequest(
    subject="<string>",
    message="<string>",
    reminder_interval="<integer>"
)

result = sdk.set_notification.set_envelope_notification(
    request_body=request_body,
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
