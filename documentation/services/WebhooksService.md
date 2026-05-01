# WebhooksService

A list of all methods in the `WebhooksService` service. Click on the method name to view detailed information about that method.

| Methods                         | Description   |
| :------------------------------ | :------------ |
| [list_webhooks](#list_webhooks) | List webhooks |

## list_webhooks

List webhooks

- HTTP Method: `POST`
- Endpoint: `/webhooks`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [ListWebhooksRequest](../models/ListWebhooksRequest.md) | ✅       | The request body. |
| accept       | str                                                     | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import ListWebhooksRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ListWebhooksRequest(
    webhook_id="string",
    event="ENVELOPE_COMPLETED"
)

result = sdk.webhooks.list_webhooks(
    request_body=request_body,
    accept="application/json"
)

print(result)
```
