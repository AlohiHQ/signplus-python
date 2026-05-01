# CertificateService

A list of all methods in the `CertificateService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                                        |
| :-------------------------------------------------------------- | :------------------------------------------------- |
| [download_envelope_certificate](#download_envelope_certificate) | Download certificate of completion for an envelope |

## download_envelope_certificate

Download certificate of completion for an envelope

- HTTP Method: `GET`
- Endpoint: `/envelope/{envelope_id}/certificate`

**Parameters**

| Name        | Type | Required | Description |
| :---------- | :--- | :------- | :---------- |
| envelope_id | str  | ✅       |             |
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

result = sdk.certificate.download_envelope_certificate(
    envelope_id="envelope_id",
    accept="application/pdf"
)

print(result)
```
