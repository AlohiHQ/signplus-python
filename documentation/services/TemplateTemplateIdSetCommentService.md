# TemplateTemplateIdSetCommentService

A list of all methods in the `TemplateTemplateIdSetCommentService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description          |
| :-------------------------------------------- | :------------------- |
| [set_template_comment](#set_template_comment) | Set template comment |

## set_template_comment

Set template comment

- HTTP Method: `PUT`
- Endpoint: `/template/{template_id}/set_comment`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SetTemplateCommentRequest](../models/SetTemplateCommentRequest.md) | ✅       | The request body. |
| template_id  | str                                                                 | ✅       |                   |
| accept       | str                                                                 | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetTemplateCommentRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetTemplateCommentRequest(
    comment="<string>"
)

result = sdk.template_template_id_set_comment.set_template_comment(
    request_body=request_body,
    template_id="template_id",
    accept="application/json"
)

print(result)
```
