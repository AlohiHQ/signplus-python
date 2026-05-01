# SetCommentService

A list of all methods in the `SetCommentService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description          |
| :-------------------------------------------- | :------------------- |
| [set_envelope_comment](#set_envelope_comment) | Set envelope comment |

## set_envelope_comment

Set envelope comment

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/set_comment`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SetEnvelopeCommentRequest](../models/SetEnvelopeCommentRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                 | ✅       |                   |
| accept       | str                                                                 | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetEnvelopeCommentRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetEnvelopeCommentRequest(
    comment="<string>"
)

result = sdk.set_comment.set_envelope_comment(
    request_body=request_body,
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
