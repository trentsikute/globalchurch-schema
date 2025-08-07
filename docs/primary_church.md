

# Slot: primary_church 


_FK → Church.church_id (the user’s primary church)._





URI: [gc:primary_church](https://global.church/schema/primary_church)
Alias: primary_church

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
| self | gc:primary_church |
| native | gc:primary_church |




## LinkML Source

<details>
```yaml
name: primary_church
description: FK → Church.church_id (the user’s primary church).
from_schema: https://global.church/schema
rank: 1000
alias: primary_church
domain_of:
- User
range: uuid

```
</details>