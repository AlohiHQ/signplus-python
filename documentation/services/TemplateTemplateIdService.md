# TemplateTemplateIdService

A list of all methods in the `TemplateTemplateIdService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description     |
| :---------------------------------- | :-------------- |
| [get_template](#get_template)       | Get template    |
| [delete_template](#delete_template) | Delete template |

## get_template

Get template

- HTTP Method: `GET`
- Endpoint: `/template/{template_id}`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| template_id | str  | ✅       |             |
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

result = sdk.template_template_id.get_template(
    template_id="template_id",
    accept="application/json"
)

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

result = sdk.template_template_id.delete_template(template_id="template_id")

print(result)
```
