# TemplateRecipient

**Properties**

| Name  | Type                  | Required | Description                                                                                                                                                                |
| :---- | :-------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_  | str                   | ❌       | Unique identifier of the recipient                                                                                                                                         |
| uid   | str                   | ❌       | Unique identifier of the user associated with the recipient                                                                                                                |
| name  | str                   | ❌       | Name of the recipient                                                                                                                                                      |
| email | str                   | ❌       | Email of the recipient                                                                                                                                                     |
| role  | TemplateRecipientRole | ❌       | Role of the recipient (SIGNER signs the document, RECEIVES_COPY receives a copy of the document, IN_PERSON_SIGNER signs the document in person, SENDER sends the document) |
