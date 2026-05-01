# SigningStepsService

A list of all methods in the `SigningStepsService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                |
| :-------------------------------------------------------- | :------------------------- |
| [add_envelope_signing_steps](#add_envelope_signing_steps) | Add envelope signing steps |

## add_envelope_signing_steps

Add envelope signing steps

- HTTP Method: `POST`
- Endpoint: `/envelope/{envelope_id}/signing_steps`

**Parameters**

| Name         | Type                                                                          | Required | Description       |
| :----------- | :---------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AddEnvelopeSigningStepsRequest](../models/AddEnvelopeSigningStepsRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                           | ✅       |                   |
| accept       | str                                                                           | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import AddEnvelopeSigningStepsRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AddEnvelopeSigningStepsRequest(
    signing_steps=[
        {
            "recipients": [
                {
                    "name": "<string>",
                    "email": "<string>",
                    "role": "IN_PERSON_SIGNER",
                    "id_": "<string>",
                    "uid": "<string>",
                    "verification": {
                        "type_": "SMS",
                        "value": "<string>"
                    }
                }
            ]
        }
    ]
)

result = sdk.signing_steps.add_envelope_signing_steps(
    request_body=request_body,
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
