

# Slot: user_id 


_Unique ID for a registered platform user._





URI: [gc:user_id](https://global.church/schema/user_id)
Alias: user_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [User](User.md) | A registered platform user |  no  |






## Properties

* Range: [Uuid](Uuid.md)

* Required: True





## Examples

| Value |
| --- |
| 550e8400-e29b-41d4-a716-446655440000 |
| 3fa85f64-5717-4562-b3fc-2c963f66afa6 |

## Comments

* This is the stable, system-issued identifier for a user.
It is used as the primary key and as the target of foreign keys in related tables.
Must be a valid UUID (v4 recommended). Never reuse or recycle a user_id.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:user_id |
| native | gc:user_id |
| exact | schema:identifier |




## LinkML Source

<details>
```yaml
name: user_id
description: Unique ID for a registered platform user.
comments:
- 'This is the stable, system-issued identifier for a user.

  It is used as the primary key and as the target of foreign keys in related tables.

  Must be a valid UUID (v4 recommended). Never reuse or recycle a user_id.

  '
examples:
- value: 550e8400-e29b-41d4-a716-446655440000
  description: Example UUID for a user record.
- value: 3fa85f64-5717-4562-b3fc-2c963f66afa6
  description: Another valid UUID.
from_schema: https://global.church/schema
exact_mappings:
- schema:identifier
rank: 1000
identifier: true
alias: user_id
domain_of:
- User
range: uuid
required: true

```
</details>