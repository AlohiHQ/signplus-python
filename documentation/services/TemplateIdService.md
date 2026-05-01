# TemplateIdService

A list of all methods in the `TemplateIdService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                       |
| :-------------------------------------------------------------- | :-------------------------------- |
| [create_envelope_from_template](#create_envelope_from_template) | Create new envelope from template |

## create_envelope_from_template

Create new envelope from template

- HTTP Method: `POST`
- Endpoint: `/envelope/from_template/{template_id}`

**Parameters**

| Name         | Type                                                                                | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateEnvelopeFromTemplateRequest](../models/CreateEnvelopeFromTemplateRequest.md) | ✅       | The request body. |
| template_id  | str                                                                                 | ✅       |                   |
| accept       | str                                                                                 | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import CreateEnvelopeFromTemplateRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateEnvelopeFromTemplateRequest(
    name="dwL1t",
    comment="string",
    sandbox=False
)

result = sdk.template_id.create_envelope_from_template(
    request_body=request_body,
    template_id="template_id",
    accept="application/json"
)

print(result)
```
