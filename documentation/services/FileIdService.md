# FileIdService

A list of all methods in the `FileIdService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description                  |
| :------------------------------------------ | :--------------------------- |
| [get_attachment_file](#get_attachment_file) | Get envelope attachment file |

## get_attachment_file

Get envelope attachment file

- HTTP Method: `GET`
- Endpoint: `/envelope/{envelope_id}/attachments/{file_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |
| file_id     | str  | ✅       |             |
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

result = sdk.file_id.get_attachment_file(
    envelope_id="envelope_id",
    file_id="file_id",
    accept="application/octet-stream"
)

print(result)
```
