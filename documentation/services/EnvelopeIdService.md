# EnvelopeIdService

A list of all methods in the `EnvelopeIdService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description     |
| :---------------------------------- | :-------------- |
| [get_envelope](#get_envelope)       | Get envelope    |
| [delete_envelope](#delete_envelope) | Delete envelope |

## get_envelope

Get envelope

- HTTP Method: `GET`
- Endpoint: `/envelope/{envelope_id}`

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

result = sdk.envelope_id.get_envelope(
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```

## delete_envelope

Delete envelope

- HTTP Method: `DELETE`
- Endpoint: `/envelope/{envelope_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |

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

result = sdk.envelope_id.delete_envelope(envelope_id="envelope_id")

print(result)
```
