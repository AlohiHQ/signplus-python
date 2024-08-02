# ListTemplatesRequest

**Properties**

| Name        | Type               | Required | Description                                   |
| :---------- | :----------------- | :------- | :-------------------------------------------- |
| name        | str                | ❌       | Name of the template                          |
| tags        | List[str]          | ❌       | List of tag templates                         |
| ids         | List[str]          | ❌       | List of templates IDs                         |
| first       | int                | ❌       |                                               |
| last        | int                | ❌       |                                               |
| after       | str                | ❌       |                                               |
| before      | str                | ❌       |                                               |
| order_field | TemplateOrderField | ❌       | Field to order templates by                   |
| ascending   | bool               | ❌       | Whether to order templates in ascending order |
