# AnnotationService

A list of all methods in the `AnnotationService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description             |
| :-------------------------------------------------- | :---------------------- |
| [add_envelope_annotation](#add_envelope_annotation) | Add envelope annotation |

## add_envelope_annotation

Add envelope annotation

- HTTP Method: `POST`
- Endpoint: `/envelope/{envelope_id}/annotation`

**Parameters**

| Name         | Type                                                                      | Required | Description       |
| :----------- | :------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [AddEnvelopeAnnotationRequest](../models/AddEnvelopeAnnotationRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                       | ✅       |                   |
| accept       | str                                                                       | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import AddEnvelopeAnnotationRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AddEnvelopeAnnotationRequest(
    document_id="<string>",
    page="<integer>",
    x="<float>",
    y="<float>",
    width="<float>",
    height="<float>",
    type_="INITIALS",
    recipient_id="<string>",
    required="<boolean>",
    signature={
        "id_": "<string>"
    },
    initials={
        "id_": "<string>"
    },
    text={
        "size": "<number>",
        "color": "<number>",
        "value": "<string>",
        "tooltip": "<string>",
        "dynamic_field_name": "<string>",
        "font": {
            "family": "SANS",
            "italic": "<boolean>",
            "bold": "<boolean>"
        }
    },
    datetime_={
        "size": "<number>",
        "font": {
            "family": "UNKNOWN",
            "italic": "<boolean>",
            "bold": "<boolean>"
        },
        "color": "<string>",
        "auto_fill": "<boolean>",
        "timezone": "<string>",
        "timestamp": "<integer>",
        "format": "YMD_NUMERIC_SLASH"
    },
    checkbox={
        "checked": "<boolean>",
        "style": "TIMES_SQUARE"
    }
)

result = sdk.annotation.add_envelope_annotation(
    request_body=request_body,
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
