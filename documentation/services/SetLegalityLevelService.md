# SetLegalityLevelService

A list of all methods in the `SetLegalityLevelService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                 |
| :---------------------------------------------------------- | :-------------------------- |
| [set_envelope_legality_level](#set_envelope_legality_level) | Set envelope legality level |

## set_envelope_legality_level

Set envelope legality level

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/set_legality_level`

**Parameters**

| Name         | Type                                                                            | Required | Description       |
| :----------- | :------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SetEnvelopeLegalityLevelRequest](../models/SetEnvelopeLegalityLevelRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                             | ✅       |                   |
| accept       | str                                                                             | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetEnvelopeLegalityLevelRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetEnvelopeLegalityLevelRequest(
    legality_level="QES_EIDAS"
)

result = sdk.set_legality_level.set_envelope_legality_level(
    request_body=request_body,
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
