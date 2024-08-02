# SignplusService

A list of all methods in the `SignplusService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                       |
| :---------------------------------------------------------------------- | :-------------------------------- |
| [create_envelope](#create_envelope)                                     | Create new envelope               |
| [create_envelope_from_template](#create_envelope_from_template)         | Create new envelope from template |
| [list_envelopes](#list_envelopes)                                       | List envelopes                    |
| [get_envelope](#get_envelope)                                           | Get envelope                      |
| [delete_envelope](#delete_envelope)                                     | Delete envelope                   |
| [get_envelope_document](#get_envelope_document)                         | Get envelope document             |
| [get_envelope_documents](#get_envelope_documents)                       | Get envelope documents            |
| [add_envelope_document](#add_envelope_document)                         | Add envelope document             |
| [set_envelope_dynamic_fields](#set_envelope_dynamic_fields)             | Set envelope dynamic fields       |
| [add_envelope_signing_steps](#add_envelope_signing_steps)               | Add envelope signing steps        |
| [send_envelope](#send_envelope)                                         | Send envelope for signature       |
| [duplicate_envelope](#duplicate_envelope)                               | Duplicate envelope                |
| [void_envelope](#void_envelope)                                         | Void envelope                     |
| [rename_envelope](#rename_envelope)                                     | Rename envelope                   |
| [set_envelope_comment](#set_envelope_comment)                           | Set envelope comment              |
| [set_envelope_notification](#set_envelope_notification)                 | Set envelope notification         |
| [set_envelope_expiration_date](#set_envelope_expiration_date)           | Set envelope expiration date      |
| [set_envelope_legality_level](#set_envelope_legality_level)             | Set envelope legality level       |
| [get_envelope_annotations](#get_envelope_annotations)                   | Get envelope annotations          |
| [get_envelope_document_annotations](#get_envelope_document_annotations) | Get envelope document annotations |
| [add_envelope_annotation](#add_envelope_annotation)                     | Add envelope annotation           |
| [delete_envelope_annotation](#delete_envelope_annotation)               | Delete envelope annotation        |
| [create_template](#create_template)                                     | Create new template               |
| [list_templates](#list_templates)                                       | List templates                    |
| [get_template](#get_template)                                           | Get template                      |
| [delete_template](#delete_template)                                     | Delete template                   |
| [duplicate_template](#duplicate_template)                               | Duplicate template                |
| [add_template_document](#add_template_document)                         | Add template document             |
| [get_template_document](#get_template_document)                         | Get template document             |
| [get_template_documents](#get_template_documents)                       | Get template documents            |
| [add_template_signing_steps](#add_template_signing_steps)               | Add template signing steps        |
| [rename_template](#rename_template)                                     | Rename template                   |
| [set_template_comment](#set_template_comment)                           | Set template comment              |
| [set_template_notification](#set_template_notification)                 | Set template notification         |
| [get_template_annotations](#get_template_annotations)                   | Get template annotations          |
| [get_document_template_annotations](#get_document_template_annotations) | Get document template annotations |
| [add_template_annotation](#add_template_annotation)                     | Add template annotation           |
| [delete_template_annotation](#delete_template_annotation)               | Delete template annotation        |
| [create_webhook](#create_webhook)                                       | Create webhook                    |
| [list_webhooks](#list_webhooks)                                         | List webhooks                     |
| [delete_webhook](#delete_webhook)                                       | Delete webhook                    |

## create_envelope

Create new envelope

- HTTP Method: `POST`
- Endpoint: `/envelope`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateEnvelopeRequest](../models/CreateEnvelopeRequest.md) | ✅       | The request body. |

**Return Type**

`Envelope`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import CreateEnvelopeRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateEnvelopeRequest(
    name="name",
    flow_type="REQUEST_SIGNATURE",
    legality_level="SES",
    expires_at=4,
    comment="comment",
    sandbox=True
)

result = sdk.signplus.create_envelope(request_body=request_body)

print(result)
```

## create_envelope_from_template

Create new envelope from template

- HTTP Method: `POST`
- Endpoint: `/envelope/from_template/{template_id}`

**Parameters**

| Name         | Type                                                                                | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateEnvelopeFromTemplateRequest](../models/CreateEnvelopeFromTemplateRequest.md) | ✅       | The request body. |
| template_id  | str                                                                                 | ✅       |                   |

**Return Type**

`Envelope`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import CreateEnvelopeFromTemplateRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateEnvelopeFromTemplateRequest(
    name="name",
    comment="comment",
    sandbox=False
)

result = sdk.signplus.create_envelope_from_template(
    request_body=request_body,
    template_id="template_id"
)

print(result)
```

## list_envelopes

List envelopes

- HTTP Method: `POST`
- Endpoint: `/envelopes`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [ListEnvelopesRequest](../models/ListEnvelopesRequest.md) | ❌       | The request body. |

**Return Type**

`ListEnvelopesResponse`

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
    name="name",
    tags=[
        "tags"
    ],
    comment="comment",
    ids=[
        "ids"
    ],
    statuses=[
        "DRAFT"
    ],
    folder_ids=[
        "folder_ids"
    ],
    only_root_folder=False,
    date_from=2,
    date_to=5,
    uid="uid",
    first=4,
    last=9,
    after="after",
    before="before",
    order_field="CREATION_DATE",
    ascending=True,
    include_trash=True
)

result = sdk.signplus.list_envelopes(request_body=request_body)

print(result)
```

## get_envelope

Get envelope

- HTTP Method: `GET`
- Endpoint: `/envelope/{envelope_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |

**Return Type**

`Envelope`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.get_envelope(envelope_id="envelope_id")

print(result)
```

## delete_envelope

Delete envelope

- HTTP Method: `DELETE`
- Endpoint: `/envelope/{envelope_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.delete_envelope(envelope_id="envelope_id")

print(result)
```

## get_envelope_document

Get envelope document

- HTTP Method: `GET`
- Endpoint: `/envelope/{envelope_id}/document/{document_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |
| document_id | str  | ✅       |             |

**Return Type**

`Document`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.get_envelope_document(
    envelope_id="envelope_id",
    document_id="document_id"
)

print(result)
```

## get_envelope_documents

Get envelope documents

- HTTP Method: `GET`
- Endpoint: `/envelope/{envelope_id}/documents`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |

**Return Type**

`ListEnvelopeDocumentsResponse`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.get_envelope_documents(envelope_id="envelope_id")

print(result)
```

## add_envelope_document

Add envelope document

- HTTP Method: `POST`
- Endpoint: `/envelope/{envelope_id}/document`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AddEnvelopeDocumentRequest](../models/AddEnvelopeDocumentRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                   | ✅       |                   |

**Return Type**

`Document`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import AddEnvelopeDocumentRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AddEnvelopeDocumentRequest(
    file="file"
)

result = sdk.signplus.add_envelope_document(
    request_body=request_body,
    envelope_id="envelope_id"
)

print(result)
```

## set_envelope_dynamic_fields

Set envelope dynamic fields

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/dynamic_fields`

**Parameters**

| Name         | Type                                                                            | Required | Description       |
| :----------- | :------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SetEnvelopeDynamicFieldsRequest](../models/SetEnvelopeDynamicFieldsRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                             | ✅       |                   |

**Return Type**

`Envelope`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetEnvelopeDynamicFieldsRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetEnvelopeDynamicFieldsRequest(
    dynamic_fields=[
        {
            "name": "name",
            "value": "value"
        }
    ]
)

result = sdk.signplus.set_envelope_dynamic_fields(
    request_body=request_body,
    envelope_id="envelope_id"
)

print(result)
```

## add_envelope_signing_steps

Add envelope signing steps

- HTTP Method: `POST`
- Endpoint: `/envelope/{envelope_id}/signing_steps`

**Parameters**

| Name         | Type                                                                          | Required | Description       |
| :----------- | :---------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AddEnvelopeSigningStepsRequest](../models/AddEnvelopeSigningStepsRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                           | ✅       |                   |

**Return Type**

`Envelope`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import AddEnvelopeSigningStepsRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AddEnvelopeSigningStepsRequest(
    signing_steps=[
        {
            "recipients": [
                {
                    "id_": "id",
                    "uid": "uid",
                    "name": "name",
                    "email": "email",
                    "role": "SIGNER",
                    "verification": {
                        "type_": "SMS",
                        "value": "value"
                    }
                }
            ]
        }
    ]
)

result = sdk.signplus.add_envelope_signing_steps(
    request_body=request_body,
    envelope_id="envelope_id"
)

print(result)
```

## send_envelope

Send envelope for signature

- HTTP Method: `POST`
- Endpoint: `/envelope/{envelope_id}/send`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |

**Return Type**

`Envelope`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.send_envelope(envelope_id="envelope_id")

print(result)
```

## duplicate_envelope

Duplicate envelope

- HTTP Method: `POST`
- Endpoint: `/envelope/{envelope_id}/duplicate`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |

**Return Type**

`Envelope`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.duplicate_envelope(envelope_id="envelope_id")

print(result)
```

## void_envelope

Void envelope

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/void`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |

**Return Type**

`Envelope`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.void_envelope(envelope_id="envelope_id")

print(result)
```

## rename_envelope

Rename envelope

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/rename`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [RenameEnvelopeRequest](../models/RenameEnvelopeRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                         | ✅       |                   |

**Return Type**

`Envelope`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import RenameEnvelopeRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = RenameEnvelopeRequest(
    name="name"
)

result = sdk.signplus.rename_envelope(
    request_body=request_body,
    envelope_id="envelope_id"
)

print(result)
```

## set_envelope_comment

Set envelope comment

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/set_comment`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SetEnvelopeCommentRequest](../models/SetEnvelopeCommentRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                 | ✅       |                   |

**Return Type**

`Envelope`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetEnvelopeCommentRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetEnvelopeCommentRequest(
    comment="comment"
)

result = sdk.signplus.set_envelope_comment(
    request_body=request_body,
    envelope_id="envelope_id"
)

print(result)
```

## set_envelope_notification

Set envelope notification

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/set_notification`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [EnvelopeNotification](../models/EnvelopeNotification.md) | ✅       | The request body. |
| envelope_id  | str                                                       | ✅       |                   |

**Return Type**

`Envelope`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import EnvelopeNotification

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = EnvelopeNotification(
    subject="subject",
    message="message",
    reminder_interval=5
)

result = sdk.signplus.set_envelope_notification(
    request_body=request_body,
    envelope_id="envelope_id"
)

print(result)
```

## set_envelope_expiration_date

Set envelope expiration date

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/set_expiration_date`

**Parameters**

| Name         | Type                                                                      | Required | Description       |
| :----------- | :------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SetEnvelopeExpirationRequest](../models/SetEnvelopeExpirationRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                       | ✅       |                   |

**Return Type**

`Envelope`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetEnvelopeExpirationRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetEnvelopeExpirationRequest(
    expires_at=2
)

result = sdk.signplus.set_envelope_expiration_date(
    request_body=request_body,
    envelope_id="envelope_id"
)

print(result)
```

## set_envelope_legality_level

Set envelope legality level

- HTTP Method: `PUT`
- Endpoint: `/envelope/{envelope_id}/set_legality_level`

**Parameters**

| Name         | Type                                                                            | Required | Description       |
| :----------- | :------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SetEnvelopeLegalityLevelRequest](../models/SetEnvelopeLegalityLevelRequest.md) | ✅       | The request body. |
| envelope_id  | str                                                                             | ✅       |                   |

**Return Type**

`Envelope`

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
    legality_level="SES"
)

result = sdk.signplus.set_envelope_legality_level(
    request_body=request_body,
    envelope_id="envelope_id"
)

print(result)
```

## get_envelope_annotations

Get envelope annotations

- HTTP Method: `GET`
- Endpoint: `/envelope/{envelope_id}/annotations`

**Parameters**

| Name        | Type | Required | Description        |
| :---------- | :--- | :------- | :----------------- |
| envelope_id | str  | ✅       | ID of the envelope |

**Return Type**

`List[Annotation]`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.get_envelope_annotations(envelope_id="envelope_id")

print(result)
```

## get_envelope_document_annotations

Get envelope document annotations

- HTTP Method: `GET`
- Endpoint: `/envelope/{envelope_id}/annotations/{document_id}`

**Parameters**

| Name        | Type | Required | Description        |
| :---------- | :--- | :------- | :----------------- |
| envelope_id | str  | ✅       | ID of the envelope |
| document_id | str  | ✅       | ID of document     |

**Return Type**

`ListEnvelopeDocumentAnnotationsResponse`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.get_envelope_document_annotations(
    envelope_id="envelope_id",
    document_id="document_id"
)

print(result)
```

## add_envelope_annotation

Add envelope annotation

- HTTP Method: `POST`
- Endpoint: `/envelope/{envelope_id}/annotation`

**Parameters**

| Name         | Type                                                      | Required | Description        |
| :----------- | :-------------------------------------------------------- | :------- | :----------------- |
| request_body | [AddAnnotationRequest](../models/AddAnnotationRequest.md) | ✅       | The request body.  |
| envelope_id  | str                                                       | ✅       | ID of the envelope |

**Return Type**

`Annotation`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import AddAnnotationRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AddAnnotationRequest(
    recipient_id="recipient_id",
    document_id="document_id",
    page=7,
    x=4.46,
    y=7.18,
    width=7.26,
    height=1.77,
    required=False,
    type_="TEXT",
    signature={
        "id_": "id"
    },
    initials={
        "id_": "id"
    },
    text={
        "size": 8.13,
        "color": 7.22,
        "value": "value",
        "tooltip": "tooltip",
        "dynamic_field_name": "dynamic_field_name",
        "font": {
            "family": "UNKNOWN",
            "italic": True,
            "bold": False
        }
    },
    datetime_={
        "size": 0.86,
        "font": {
            "family": "UNKNOWN",
            "italic": True,
            "bold": False
        },
        "color": "color",
        "auto_fill": False,
        "timezone": "timezone",
        "timestamp": 8,
        "format": "DMY_NUMERIC_SLASH"
    },
    checkbox={
        "checked": False,
        "style": "CIRCLE_CHECK"
    }
)

result = sdk.signplus.add_envelope_annotation(
    request_body=request_body,
    envelope_id="envelope_id"
)

print(result)
```

## delete_envelope_annotation

Delete envelope annotation

- HTTP Method: `DELETE`
- Endpoint: `/envelope/{envelope_id}/annotation/{annotation_id}`

**Parameters**

| Name          | Type | Required | Description                    |
| :------------ | :--- | :------- | :----------------------------- |
| envelope_id   | str  | ✅       | ID of the envelope             |
| annotation_id | str  | ✅       | ID of the annotation to delete |

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.delete_envelope_annotation(
    envelope_id="envelope_id",
    annotation_id="annotation_id"
)

print(result)
```

## create_template

Create new template

- HTTP Method: `POST`
- Endpoint: `/template`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateTemplateRequest](../models/CreateTemplateRequest.md) | ✅       | The request body. |

**Return Type**

`Template`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import CreateTemplateRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateTemplateRequest(
    name="name"
)

result = sdk.signplus.create_template(request_body=request_body)

print(result)
```

## list_templates

List templates

- HTTP Method: `POST`
- Endpoint: `/templates`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [ListTemplatesRequest](../models/ListTemplatesRequest.md) | ❌       | The request body. |

**Return Type**

`ListTemplatesResponse`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import ListTemplatesRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ListTemplatesRequest(
    name="name",
    tags=[
        "tags"
    ],
    ids=[
        "ids"
    ],
    first=8,
    last=7,
    after="after",
    before="before",
    order_field="TEMPLATE_ID",
    ascending=True
)

result = sdk.signplus.list_templates(request_body=request_body)

print(result)
```

## get_template

Get template

- HTTP Method: `GET`
- Endpoint: `/template/{template_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| template_id | str  | ✅       |             |

**Return Type**

`Template`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.get_template(template_id="template_id")

print(result)
```

## delete_template

Delete template

- HTTP Method: `DELETE`
- Endpoint: `/template/{template_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| template_id | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.delete_template(template_id="template_id")

print(result)
```

## duplicate_template

Duplicate template

- HTTP Method: `POST`
- Endpoint: `/template/{template_id}/duplicate`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| template_id | str  | ✅       |             |

**Return Type**

`Template`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.duplicate_template(template_id="template_id")

print(result)
```

## add_template_document

Add template document

- HTTP Method: `POST`
- Endpoint: `/template/{template_id}/document`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AddTemplateDocumentRequest](../models/AddTemplateDocumentRequest.md) | ✅       | The request body. |
| template_id  | str                                                                   | ✅       |                   |

**Return Type**

`Document`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import AddTemplateDocumentRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AddTemplateDocumentRequest(
    file="file"
)

result = sdk.signplus.add_template_document(
    request_body=request_body,
    template_id="template_id"
)

print(result)
```

## get_template_document

Get template document

- HTTP Method: `GET`
- Endpoint: `/template/{template_id}/document/{document_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| template_id | str  | ✅       |             |
| document_id | str  | ✅       |             |

**Return Type**

`Document`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.get_template_document(
    template_id="template_id",
    document_id="document_id"
)

print(result)
```

## get_template_documents

Get template documents

- HTTP Method: `GET`
- Endpoint: `/template/{template_id}/documents`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| template_id | str  | ✅       |             |

**Return Type**

`ListTemplateDocumentsResponse`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.get_template_documents(template_id="template_id")

print(result)
```

## add_template_signing_steps

Add template signing steps

- HTTP Method: `POST`
- Endpoint: `/template/{template_id}/signing_steps`

**Parameters**

| Name         | Type                                                                          | Required | Description       |
| :----------- | :---------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AddTemplateSigningStepsRequest](../models/AddTemplateSigningStepsRequest.md) | ✅       | The request body. |
| template_id  | str                                                                           | ✅       |                   |

**Return Type**

`Template`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import AddTemplateSigningStepsRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AddTemplateSigningStepsRequest(
    signing_steps=[
        {
            "recipients": [
                {
                    "id_": "id",
                    "uid": "uid",
                    "name": "name",
                    "email": "email",
                    "role": "SIGNER"
                }
            ]
        }
    ]
)

result = sdk.signplus.add_template_signing_steps(
    request_body=request_body,
    template_id="template_id"
)

print(result)
```

## rename_template

Rename template

- HTTP Method: `PUT`
- Endpoint: `/template/{template_id}/rename`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [RenameTemplateRequest](../models/RenameTemplateRequest.md) | ✅       | The request body. |
| template_id  | str                                                         | ✅       |                   |

**Return Type**

`Template`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import RenameTemplateRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = RenameTemplateRequest(
    name="name"
)

result = sdk.signplus.rename_template(
    request_body=request_body,
    template_id="template_id"
)

print(result)
```

## set_template_comment

Set template comment

- HTTP Method: `PUT`
- Endpoint: `/template/{template_id}/set_comment`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SetTemplateCommentRequest](../models/SetTemplateCommentRequest.md) | ✅       | The request body. |
| template_id  | str                                                                 | ✅       |                   |

**Return Type**

`Template`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import SetTemplateCommentRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = SetTemplateCommentRequest(
    comment="comment"
)

result = sdk.signplus.set_template_comment(
    request_body=request_body,
    template_id="template_id"
)

print(result)
```

## set_template_notification

Set template notification

- HTTP Method: `PUT`
- Endpoint: `/template/{template_id}/set_notification`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [EnvelopeNotification](../models/EnvelopeNotification.md) | ✅       | The request body. |
| template_id  | str                                                       | ✅       |                   |

**Return Type**

`Template`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import EnvelopeNotification

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = EnvelopeNotification(
    subject="subject",
    message="message",
    reminder_interval=5
)

result = sdk.signplus.set_template_notification(
    request_body=request_body,
    template_id="template_id"
)

print(result)
```

## get_template_annotations

Get template annotations

- HTTP Method: `GET`
- Endpoint: `/template/{template_id}/annotations`

**Parameters**

| Name        | Type | Required | Description        |
| :---------- | :--- | :------- | :----------------- |
| template_id | str  | ✅       | ID of the template |

**Return Type**

`ListTemplateAnnotationsResponse`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.get_template_annotations(template_id="template_id")

print(result)
```

## get_document_template_annotations

Get document template annotations

- HTTP Method: `GET`
- Endpoint: `/template/{template_id}/annotations/{document_id}`

**Parameters**

| Name        | Type | Required | Description        |
| :---------- | :--- | :------- | :----------------- |
| template_id | str  | ✅       | ID of the template |
| document_id | str  | ✅       | ID of document     |

**Return Type**

`ListTemplateDocumentAnnotationsResponse`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.get_document_template_annotations(
    template_id="template_id",
    document_id="document_id"
)

print(result)
```

## add_template_annotation

Add template annotation

- HTTP Method: `POST`
- Endpoint: `/template/{template_id}/annotation`

**Parameters**

| Name         | Type                                                      | Required | Description        |
| :----------- | :-------------------------------------------------------- | :------- | :----------------- |
| request_body | [AddAnnotationRequest](../models/AddAnnotationRequest.md) | ✅       | The request body.  |
| template_id  | str                                                       | ✅       | ID of the template |

**Return Type**

`Annotation`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import AddAnnotationRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = AddAnnotationRequest(
    recipient_id="recipient_id",
    document_id="document_id",
    page=7,
    x=4.46,
    y=7.18,
    width=7.26,
    height=1.77,
    required=False,
    type_="TEXT",
    signature={
        "id_": "id"
    },
    initials={
        "id_": "id"
    },
    text={
        "size": 8.13,
        "color": 7.22,
        "value": "value",
        "tooltip": "tooltip",
        "dynamic_field_name": "dynamic_field_name",
        "font": {
            "family": "UNKNOWN",
            "italic": True,
            "bold": False
        }
    },
    datetime_={
        "size": 0.86,
        "font": {
            "family": "UNKNOWN",
            "italic": True,
            "bold": False
        },
        "color": "color",
        "auto_fill": False,
        "timezone": "timezone",
        "timestamp": 8,
        "format": "DMY_NUMERIC_SLASH"
    },
    checkbox={
        "checked": False,
        "style": "CIRCLE_CHECK"
    }
)

result = sdk.signplus.add_template_annotation(
    request_body=request_body,
    template_id="template_id"
)

print(result)
```

## delete_template_annotation

Delete template annotation

- HTTP Method: `DELETE`
- Endpoint: `/template/{template_id}/annotation/{annotation_id}`

**Parameters**

| Name          | Type | Required | Description                    |
| :------------ | :--- | :------- | :----------------------------- |
| template_id   | str  | ✅       | ID of the template             |
| annotation_id | str  | ✅       | ID of the annotation to delete |

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.delete_template_annotation(
    template_id="template_id",
    annotation_id="annotation_id"
)

print(result)
```

## create_webhook

Create webhook

- HTTP Method: `POST`
- Endpoint: `/webhook`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateWebhookRequest](../models/CreateWebhookRequest.md) | ✅       | The request body. |

**Return Type**

`Webhook`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import CreateWebhookRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateWebhookRequest(
    event="ENVELOPE_EXPIRED",
    target="target"
)

result = sdk.signplus.create_webhook(request_body=request_body)

print(result)
```

## list_webhooks

List webhooks

- HTTP Method: `POST`
- Endpoint: `/webhooks`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [ListWebhooksRequest](../models/ListWebhooksRequest.md) | ❌       | The request body. |

**Return Type**

`ListWebhooksResponse`

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment
from signplus.models import ListWebhooksRequest

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ListWebhooksRequest(
    webhook_id="webhook_id",
    event="ENVELOPE_EXPIRED"
)

result = sdk.signplus.list_webhooks(request_body=request_body)

print(result)
```

## delete_webhook

Delete webhook

- HTTP Method: `DELETE`
- Endpoint: `/webhook/{webhook_id}`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| webhook_id | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.signplus.delete_webhook(webhook_id="webhook_id")

print(result)
```
