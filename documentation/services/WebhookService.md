# WebhookService

A list of all methods in the `WebhookService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description    |
| :-------------------------------- | :------------- |
| [create_webhook](#create_webhook) | Create webhook |

## create_webhook

Create webhook

- HTTP Method: `POST`
- Endpoint: `/webhook`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateWebhookRequest](../models/CreateWebhookRequest.md) | ✅       | The request body. |
| accept       | str                                                       | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import CreateWebhookRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateWebhookRequest(
    event="ENVELOPE_AUDIT_TRAIL",
    target="string"
)

result = sdk.webhook.create_webhook(
    request_body=request_body,
    accept="application/json"
)

print(result)
```
