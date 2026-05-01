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

result = sdk.template_template_id_annotation.add_template_annotation(
    request_body=request_body,
    template_id="template_id",
    accept="application/json"
)

print(result)
```
