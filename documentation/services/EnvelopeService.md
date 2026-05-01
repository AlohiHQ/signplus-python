# EnvelopeService

A list of all methods in the `EnvelopeService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description         |
| :---------------------------------- | :------------------ |
| [create_envelope](#create_envelope) | Create new envelope |

## create_envelope

Create new envelope

- HTTP Method: `POST`
- Endpoint: `/envelope`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateEnvelopeRequest](../models/CreateEnvelopeRequest.md) | ✅       | The request body. |
| accept       | str                                                         | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import CreateEnvelopeRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateEnvelopeRequest(
    name="PNeiZUQ9LB9",
    legality_level="QES_ZERTES",
    expires_at="<integer>",
    comment="<string>",
    sandbox=False
)

result = sdk.envelope.create_envelope(
    request_body=request_body,
    accept="application/json"
)

print(result)
```
