# EnvelopesService

A list of all methods in the `EnvelopesService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description    |
| :-------------------------------- | :------------- |
| [list_envelopes](#list_envelopes) | List envelopes |

## list_envelopes

List envelopes

- HTTP Method: `POST`
- Endpoint: `/envelopes`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [ListEnvelopesRequest](../models/ListEnvelopesRequest.md) | ✅       | The request body. |
| accept       | str                                                       | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import ListEnvelopesRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ListEnvelopesRequest(
    name="string",
    tags=[
        "string"
    ],
    comment="string",
    ids=[
        "string"
    ],
    statuses=[
        "DRAFT"
    ],
    folder_ids=[
        "string"
    ],
    only_root_folder=False,
    date_from=6508,
    date_to=690,
    uid="string",
    first=6875,
    last=4384,
    after="string",
    before="string",
    order_field="LAST_DOCUMENT_CHANGE",
    ascending=False,
    include_trash=False
)

result = sdk.envelopes.list_envelopes(
    request_body=request_body,
    accept="application/json"
)

print(result)
```
