# ListEnvelopesRequest

**Properties**

| Name             | Type                 | Required | Description                                       |
| :--------------- | :------------------- | :------- | :------------------------------------------------ |
| name             | str                  | ❌       | Name of the envelope                              |
| tags             | List[str]            | ❌       | List of tags                                      |
| comment          | str                  | ❌       | Comment of the envelope                           |
| ids              | List[str]            | ❌       | List of envelope IDs                              |
| statuses         | List[EnvelopeStatus] | ❌       | List of envelope statuses                         |
| folder_ids       | List[str]            | ❌       | List of folder IDs                                |
| only_root_folder | bool                 | ❌       | Whether to only list envelopes in the root folder |
| date_from        | int                  | ❌       | Unix timestamp of the start date                  |
| date_to          | int                  | ❌       | Unix timestamp of the end date                    |
| uid              | str                  | ❌       | Unique identifier of the user                     |
| first            | int                  | ❌       |                                                   |
| last             | int                  | ❌       |                                                   |
| after            | str                  | ❌       |                                                   |
| before           | str                  | ❌       |                                                   |
| order_field      | EnvelopeOrderField   | ❌       | Field to order envelopes by                       |
| ascending        | bool                 | ❌       | Whether to order envelopes in ascending order     |
| include_trash    | bool                 | ❌       | Whether to include envelopes in the trash         |
