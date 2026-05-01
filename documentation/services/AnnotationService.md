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
    document_id="string",
    page=6387,
    x=4410.13346533615,
    y=5148.888749329143,
    width=3756.0248729763225,
    height=4178.76189579703,
    type_="INITIALS",
    recipient_id="string",
    required=False,
    signature={
        "id_": "string"
    },
    initials={
        "id_": "string"
    },
    text={
        "size": 6190.822136605691,
        "color": 6489.781325519173,
        "value": "string",
        "tooltip": "string",
        "dynamic_field_name": "string",
        "font": {
            "family": "SANS",
            "italic": False,
            "bold": False
        }
    },
    datetime_={
        "size": 3773.1065479576364,
        "font": {
            "family": "SERIF",
            "italic": False,
            "bold": False
        },
        "color": "string",
        "auto_fill": True,
        "timezone": "string",
        "timestamp": 6868,
        "format": "MDY_TEXT_SPACE_SHORT"
    },
    checkbox={
        "checked": False,
        "style": "SQUARE_CHECK"
    }
)

result = sdk.annotation.add_envelope_annotation(
    request_body=request_body,
    envelope_id="envelope_id",
    accept="application/json"
)

print(result)
```
