# TemplateTemplateIdAnnotationAnnotationIdService

A list of all methods in the `TemplateTemplateIdAnnotationAnnotationIdService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                |
| :-------------------------------------------------------- | :------------------------- |
| [delete_template_annotation](#delete_template_annotation) | Delete template annotation |

## delete_template_annotation

Delete template annotation

- HTTP Method: `DELETE`
- Endpoint: `/template/{template_id}/annotation/{annotation_id}`

**Parameters**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| template_id   | str  | ✅       |             |
| annotation_id | str  | ✅       |             |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.template_template_id_annotation_annotation_id.delete_template_annotation(
    template_id="template_id",
    annotation_id="annotation_id"
)

print(result)
```
