# TemplateTemplateIdSigningStepsService

A list of all methods in the `TemplateTemplateIdSigningStepsService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                |
| :-------------------------------------------------------- | :------------------------- |
| [add_template_signing_steps](#add_template_signing_steps) | Add template signing steps |

## add_template_signing_steps

Add template signing steps

- HTTP Method: `POST`
- Endpoint: `/template/{template_id}/signing_steps`

**Parameters**

| Name         | Type                                                                          | Required | Description       |
| :----------- | :---------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AddTemplateSigningStepsRequest](../models/AddTemplateSigningStepsRequest.md) | ✅       | The request body. |
| template_id  | str                                                                           | ✅       |                   |
| accept       | str                                                                           | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import AddTemplateSigningStepsRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AddTemplateSigningStepsRequest(
    signing_steps=[
        {
            "recipients": [
                {
                    "id_": "<string>",
                    "uid": "<string>",
                    "name": "<string>",
                    "email": "<string>",
                    "role": "SIGNER"
                }
            ]
        }
    ]
)

result = sdk.template_template_id_signing_steps.add_template_signing_steps(
    request_body=request_body,
    template_id="template_id",
    accept="application/json"
)

print(result)
```
