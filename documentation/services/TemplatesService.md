# TemplatesService

A list of all methods in the `TemplatesService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description    |
| :-------------------------------- | :------------- |
| [list_templates](#list_templates) | List templates |

## list_templates

List templates

- HTTP Method: `POST`
- Endpoint: `/templates`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [ListTemplatesRequest](../models/ListTemplatesRequest.md) | ✅       | The request body. |
| accept       | str                                                       | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import ListTemplatesRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ListTemplatesRequest(
    name="string",
    tags=[
        "string"
    ],
    ids=[
        "string"
    ],
    first=7297,
    last=8379,
    after="string",
    before="string",
    order_field="TEMPLATE_NAME",
    ascending=False
)

result = sdk.templates.list_templates(
    request_body=request_body,
    accept="application/json"
)

print(result)
```
