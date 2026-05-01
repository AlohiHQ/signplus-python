# TemplateTemplateIdAnnotationService

A list of all methods in the `TemplateTemplateIdAnnotationService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description             |
| :-------------------------------------------------- | :---------------------- |
| [add_template_annotation](#add_template_annotation) | Add template annotation |

## add_template_annotation

Add template annotation

- HTTP Method: `POST`
- Endpoint: `/template/{template_id}/annotation`

**Parameters**

| Name         | Type                                                                      | Required | Description       |
| :----------- | :------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [AddTemplateAnnotationRequest](../models/AddTemplateAnnotationRequest.md) | ✅       | The request body. |
| template_id  | str                                                                       | ✅       |                   |
| accept       | str                                                                       | ✅       |                   |

**Return Type**

`Any`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import AddTemplateAnnotationRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AddTemplateAnnotationRequest(
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

result = sdk.template_template_id_annotation.add_template_annotation(
    request_body=request_body,
    template_id="template_id",
    accept="application/json"
)

print(result)
```
