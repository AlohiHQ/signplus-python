# SendService

A list of all methods in the `SendService` service. Click on the method name to view detailed information about that method.

| Methods                         | Description                 |
| :------------------------------ | :-------------------------- |
| [send_envelope](#send_envelope) | Send envelope for signature |

## send_envelope

Send envelope for signature

- HTTP Method: `POST`
- Endpoint: `/envelope/{envelope_id}/send`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |
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

result = sdk.send.send_envelope(
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
