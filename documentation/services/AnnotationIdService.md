# AnnotationIdService

A list of all methods in the `AnnotationIdService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                |
| :-------------------------------------------------------- | :------------------------- |
| [delete_envelope_annotation](#delete_envelope_annotation) | Delete envelope annotation |

## delete_envelope_annotation

Delete envelope annotation

- HTTP Method: `DELETE`
- Endpoint: `/envelope/{envelope_id}/annotation/{annotation_id}`

**Parameters**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| envelope_id   | str  | ✅       |             |
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

result = sdk.annotation_id.delete_envelope_annotation(
    envelope_id="envelope_id",
    annotation_id="annotation_id"
)

print(result)
```
