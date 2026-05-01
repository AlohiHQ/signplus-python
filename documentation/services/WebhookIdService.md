# WebhookIdService

A list of all methods in the `WebhookIdService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description    |
| :-------------------------------- | :------------- |
| [delete_webhook](#delete_webhook) | Delete webhook |

## delete_webhook

Delete webhook

- HTTP Method: `DELETE`
- Endpoint: `/webhook/{webhook_id}`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| webhook_id | str  | ✅       |             |

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

result = sdk.webhook_id.delete_webhook(webhook_id="webhook_id")

print(result)
```
