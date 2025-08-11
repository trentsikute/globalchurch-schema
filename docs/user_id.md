

# Slot: user_id 


_Primary key for User (also referenced by other tables)._





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
description: Primary key for User (also referenced by other tables).
in_subset:
- public
- user_core
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