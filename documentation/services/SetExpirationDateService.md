# SetExpirationDateService

A list of all methods in the `SetExpirationDateService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                  |
| :------------------------------------------------------------ | :--------------------------- |
| [set_envelope_expiration_date](#set_envelope_expiration_date) | Set envelope expiration date |

## set_envelope_expiration_date

Set envelope expiration date

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/set_expiration_date`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [SetEnvelopeExpirationDateRequest](../models/SetEnvelopeExpirationDateRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                               | ✅       |                   |
| accept       | str                                                                               | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetEnvelopeExpirationDateRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetEnvelopeExpirationDateRequest(
    expires_at="<integer>"
)

result = sdk.set_expiration_date.set_envelope_expiration_date(
    request_body=request_body,
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
