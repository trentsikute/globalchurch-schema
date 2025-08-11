

# Slot: alternate_church 


_Optional FK → Church.church_id (secondary church)._





URI: [gc:alternate_church](https://global.church/schema/alternate_church)
Alias: alternate_church

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [User](User.md) | A registered platform user |  no  |






## Properties

* Range: [Uuid](Uuid.md)




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
description: Optional FK → Church.church_id (secondary church).
in_subset:
- internal
from_schema: https://global.church/schema
rank: 1000
alias: alternate_church
domain_of:
- User
range: uuid

```
</details>