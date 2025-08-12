

# Slot: alternate_church 


_Optional FK to a secondary/alternate Church._





URI: [gc:alternate_church](https://global.church/schema/alternate_church)
Alias: alternate_church

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [User](User.md) | A registered platform user |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| 3fa85f64-5717-4562-b3fc-2c963f66afa6 |
| 00000000-0000-0000-0000-000000000000 |

## Comments

* Points to `Church.church_id`. Use when a user has a secondary affiliation
(e.g., a campus they visit occasionally). Leave empty if not applicable.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:alternate_church |
| native | gc:alternate_church |




## LinkML Source

<details>
```yaml
name: alternate_church
description: Optional FK to a secondary/alternate Church.
comments:
- 'Points to `Church.church_id`. Use when a user has a secondary affiliation

  (e.g., a campus they visit occasionally). Leave empty if not applicable.

  '
examples:
- value: 3fa85f64-5717-4562-b3fc-2c963f66afa6
  description: UUID of an alternate church.
- value: 00000000-0000-0000-0000-000000000000
  description: Empty/placeholder not valid—use null instead.
from_schema: https://global.church/schema
rank: 1000
alias: alternate_church
domain_of:
- User
range: string

```
</details>