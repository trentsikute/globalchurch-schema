

# Slot: primary_church 


_FK to the user’s primary Church._





URI: [gc:primary_church](https://global.church/schema/primary_church)
Alias: primary_church

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [User](User.md) | A registered platform user |  no  |







## Properties

* Range: [Uuid](Uuid.md)






## Examples

| Value |
| --- |
| a4b7b3a1-2c6e-4b0a-8c0a-2d6e5c9a2f11 |

## Comments

* Points to `Church.church_id`. Use when a user affiliates with a single congregation.
If the user participates at multiple churches, consider also setting `alternate_church`.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:primary_church |
| native | gc:primary_church |




## LinkML Source

<details>
```yaml
name: primary_church
description: FK to the user’s primary Church.
comments:
- 'Points to `Church.church_id`. Use when a user affiliates with a single congregation.

  If the user participates at multiple churches, consider also setting `alternate_church`.

  '
examples:
- value: a4b7b3a1-2c6e-4b0a-8c0a-2d6e5c9a2f11
  description: UUID of the primary church.
in_subset:
- private
from_schema: https://global.church/schema
rank: 1000
alias: primary_church
domain_of:
- User
range: uuid

```
</details>