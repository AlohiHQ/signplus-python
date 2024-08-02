# AddAnnotationRequest

**Properties**

| Name         | Type                | Required | Description                                                                                     |
| :----------- | :------------------ | :------- | :---------------------------------------------------------------------------------------------- |
| document_id  | str                 | ✅       | ID of the document                                                                              |
| page         | int                 | ✅       | Page number where the annotation is placed                                                      |
| x            | float               | ✅       | X coordinate of the annotation (in % of the page width from 0 to 100) from the top left corner  |
| y            | float               | ✅       | Y coordinate of the annotation (in % of the page height from 0 to 100) from the top left corner |
| width        | float               | ✅       | Width of the annotation (in % of the page width from 0 to 100)                                  |
| height       | float               | ✅       | Height of the annotation (in % of the page height from 0 to 100)                                |
| type\_       | AnnotationType      | ✅       | Type of the annotation                                                                          |
| recipient_id | str                 | ❌       | ID of the recipient                                                                             |
| required     | bool                | ❌       |                                                                                                 |
| signature    | AnnotationSignature | ❌       | Signature annotation (null if annotation is not a signature)                                    |
| initials     | AnnotationInitials  | ❌       | Initials annotation (null if annotation is not initials)                                        |
| text         | AnnotationText      | ❌       | Text annotation (null if annotation is not a text)                                              |
| datetime\_   | AnnotationDateTime  | ❌       | Date annotation (null if annotation is not a date)                                              |
| checkbox     | AnnotationCheckbox  | ❌       | Checkbox annotation (null if annotation is not a checkbox)                                      |
