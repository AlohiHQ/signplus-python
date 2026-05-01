# TemplateService

A list of all methods in the `TemplateService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description         |
| :---------------------------------- | :------------------ |
| [create_template](#create_template) | Create new template |

## create_template

Create new template

- HTTP Method: `POST`
- Endpoint: `/template`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateTemplateRequest](../models/CreateTemplateRequest.md) | ✅       | The request body. |
| accept       | str                                                         | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import CreateTemplateRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateTemplateRequest(
    name="rEATXel"
)

result = sdk.template.create_template(
    request_body=request_body,
    accept="application/json"
)

print(result)
```
