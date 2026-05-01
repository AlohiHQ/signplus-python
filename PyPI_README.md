# Signplus Python SDK 3.0.0<a id="signplus-python-sdk-300"></a>

Welcome to the Signplus SDK documentation. This guide will help you get started with integrating and using the Signplus SDK in your project.

## Versions<a id="versions"></a>

- API version: `2.5.0`
- SDK version: `3.0.0`

## About the API<a id="about-the-api"></a>

Integrate legally-binding electronic signature to your workflow

Contact Support:
Name: Sign.Plus
Email: support@alohi.com

## Table of Contents<a id="table-of-contents"></a>

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Authentication](#authentication)
  - [Access Token Authentication](#access-token-authentication)
- [Setting a Custom Timeout](#setting-a-custom-timeout)
- [Sample Usage](#sample-usage)
- [Services](#services)
- [Models](#models)
- [License](#license)

# Setup & Configuration<a id="setup--configuration"></a>

## Supported Language Versions<a id="supported-language-versions"></a>

This SDK is compatible with the following versions: `Python >= 3.7`

## Installation<a id="installation"></a>

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install signplus-python
```

If you are using Python 3, you can use `pip3` instead:

```bash
pip3 install signplus-python
```

## Authentication<a id="authentication"></a>

### Access Token Authentication<a id="access-token-authentication"></a>

The Signplus API uses an Access Token for authentication.

This token must be provided to authenticate your requests to the API.

#### Setting the Access Token<a id="setting-the-access-token"></a>

When you initialize the SDK, you can set the access token as follows:

```py
Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    timeout=10000
)
```

If you need to set or update the access token after initializing the SDK, you can use:

```py
sdk.set_access_token("YOUR_ACCESS_TOKEN")
```

## Setting a Custom Timeout<a id="setting-a-custom-timeout"></a>

You can set a custom timeout for the SDK's HTTP requests as follows:

```py
from signplus import Signplus

sdk = Signplus(timeout=10000)
```

# Sample Usage<a id="sample-usage"></a>

Below is a comprehensive example demonstrating how to authenticate and call a simple endpoint:

```py
from signplus import Signplus, Environment

sdk = Signplus(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.envelope_id.delete_envelope(envelope_id="envelope_id")

print(result)

```

# Async Usage<a id="async-usage"></a>

The SDK includes an Async Client for making asynchronous API requests. This is useful for applications that need non-blocking operations, like web servers or apps with a graphical user interface.

```py
import asyncio
from signplus import SignplusAsync, Environment

sdk = SignplusAsync(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)


async def main():
  result = await sdk.envelope_id.get_envelope(
    envelope_id="envelope_id",
    accept="application/json"
)
  print(result)

asyncio.run(main())
```

## Services<a id="services"></a>

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services:</summary>

| Name                                          |
| :-------------------------------------------- |
| template_id                                   |
| signed_documents                              |
| certificate                                   |
| document_id                                   |
| document                                      |
| documents                                     |
| dynamic_fields                                |
| signing_steps                                 |
| settings                                      |
| placeholders                                  |
| file_id                                       |
| send                                          |
| duplicate                                     |
| void                                          |
| rename                                        |
| set_comment                                   |
| set_notification                              |
| set_expiration_date                           |
| set_legality_level                            |
| envelope_envelope_id_annotations_document_id  |
| annotations                                   |
| annotation_id                                 |
| annotation                                    |
| envelope_id                                   |
| envelope                                      |
| envelopes                                     |
| template_template_id_duplicate                |
| template_template_id_document_document_id     |
| template_template_id_document                 |
| template_template_id_documents                |
| template_template_id_signing_steps            |
| template_template_id_rename                   |
| template_template_id_set_comment              |
| template_template_id_set_notification         |
| template_template_id_annotations_document_id  |
| template_template_id_annotations              |
| template_template_id_annotation_annotation_id |
| template_template_id_annotation               |
| template_template_id_attachments_settings     |
| template_template_id_attachments_placeholders |
| template_template_id                          |
| template                                      |
| templates                                     |
| webhook_id                                    |
| webhook                                       |
| webhooks                                      |

</details>

## Models<a id="models"></a>

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models:</summary>

| Name                                                  | Description |
| :---------------------------------------------------- | :---------- |
| CreateEnvelopeFromTemplateRequest                     |             |
| AddEnvelopeDocumentRequest                            |             |
| SetEnvelopeDynamicFieldsRequest                       |             |
| AddEnvelopeSigningStepsRequest                        |             |
| SetEnvelopeAttachmentsSettingsRequest                 |             |
| SetEnvelopeAttachmentsPlaceholdersRequest             |             |
| RenameEnvelopeRequest                                 |             |
| SetEnvelopeCommentRequest                             |             |
| SetEnvelopeNotificationRequest                        |             |
| SetEnvelopeExpirationDateRequest                      |             |
| SetEnvelopeLegalityLevelRequest                       |             |
| AddEnvelopeAnnotationRequest                          |             |
| CreateEnvelopeRequest                                 |             |
| ListEnvelopesRequest                                  |             |
| AddTemplateDocumentRequest                            |             |
| AddTemplateSigningStepsRequest                        |             |
| RenameTemplateRequest                                 |             |
| SetTemplateCommentRequest                             |             |
| SetTemplateNotificationRequest                        |             |
| AddTemplateAnnotationRequest                          |             |
| SetTemplateAttachmentsSettingsRequest                 |             |
| SetTemplateAttachmentsPlaceholdersRequest             |             |
| CreateTemplateRequest                                 |             |
| ListTemplatesRequest                                  |             |
| CreateWebhookRequest                                  |             |
| ListWebhooksRequest                                   |             |
| DynamicFields                                         |             |
| AddEnvelopeSigningStepsRequestSigningSteps            |             |
| SigningStepsRecipients1                               |             |
| Verification                                          |             |
| SetEnvelopeAttachmentsSettingsRequestSettings         |             |
| SetEnvelopeAttachmentsPlaceholdersRequestPlaceholders |             |
| AddEnvelopeAnnotationRequestSignature                 |             |
| AddEnvelopeAnnotationRequestInitials                  |             |
| AddEnvelopeAnnotationRequestText                      |             |
| AddEnvelopeAnnotationRequestDatetime                  |             |
| AddEnvelopeAnnotationRequestCheckbox                  |             |
| TextFont1                                             |             |
| DatetimeFont1                                         |             |
| AddTemplateSigningStepsRequestSigningSteps            |             |
| SigningStepsRecipients2                               |             |
| AddTemplateAnnotationRequestSignature                 |             |
| AddTemplateAnnotationRequestInitials                  |             |
| AddTemplateAnnotationRequestText                      |             |
| AddTemplateAnnotationRequestDatetime                  |             |
| AddTemplateAnnotationRequestCheckbox                  |             |
| TextFont2                                             |             |
| DatetimeFont2                                         |             |
| SetTemplateAttachmentsSettingsRequestSettings         |             |
| SetTemplateAttachmentsPlaceholdersRequestPlaceholders |             |

</details>

## License<a id="license"></a>

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.
