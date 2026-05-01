# AnnotationsService

A list of all methods in the `AnnotationsService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description              |
| :---------------------------------------------------- | :----------------------- |
| [get_envelope_annotations](#get_envelope_annotations) | Get envelope annotations |

## get_envelope_annotations

Get envelope annotations

- HTTP Method: `GET`
- Endpoint: `/envelope/{envelope_id}/annotations`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |
| accept      | str  | ✅       |             |

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

result = sdk.annotations.get_envelope_annotations(
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
