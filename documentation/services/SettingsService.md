# SettingsService

A list of all methods in the `SettingsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                      |
| :---------------------------------------------------------------------- | :------------------------------- |
| [set_envelope_attachments_settings](#set_envelope_attachments_settings) | Set envelope attachment settings |

## set_envelope_attachments_settings

Set envelope attachment settings

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/attachments/settings`

**Parameters**

| Name         | Type                                                                                        | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SetEnvelopeAttachmentsSettingsRequest](../models/SetEnvelopeAttachmentsSettingsRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                                         | ✅       |                   |
| accept       | str                                                                                         | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetEnvelopeAttachmentsSettingsRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetEnvelopeAttachmentsSettingsRequest(
    settings={
        "visible_to_recipients": "<boolean>"
    }
)

result = sdk.settings.set_envelope_attachments_settings(
    request_body=request_body,
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
