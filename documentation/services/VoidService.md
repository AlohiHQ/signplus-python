# VoidService

A list of all methods in the `VoidService` service. Click on the method name to view detailed information about that method.

| Methods                         | Description   |
| :------------------------------ | :------------ |
| [void_envelope](#void_envelope) | Void envelope |

## void_envelope

Void envelope

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/void`

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

result = sdk.void.void_envelope(
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
