# DynamicFieldsService

A list of all methods in the `DynamicFieldsService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                 |
| :---------------------------------------------------------- | :-------------------------- |
| [set_envelope_dynamic_fields](#set_envelope_dynamic_fields) | Set envelope dynamic fields |

## set_envelope_dynamic_fields

Set envelope dynamic fields

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/dynamic_fields`

**Parameters**

| Name         | Type                                                                            | Required | Description       |
| :----------- | :------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SetEnvelopeDynamicFieldsRequest](../models/SetEnvelopeDynamicFieldsRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                             | ✅       |                   |
| accept       | str                                                                             | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetEnvelopeDynamicFieldsRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetEnvelopeDynamicFieldsRequest(
    dynamic_fields=[
        {
            "name": "<string>",
            "value": "<string>"
        }
    ]
)

result = sdk.dynamic_fields.set_envelope_dynamic_fields(
    request_body=request_body,
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
