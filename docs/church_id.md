

# Slot: church_id 


_Primary key for Church; referenced by related tables._





URI: [gc:church_id](https://global.church/schema/church_id)
Alias: church_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  no  |






## Properties

* Range: [Uuid](Uuid.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:church_id |
| native | gc:church_id |




## LinkML Source

<details>
```yaml
name: church_id
description: Primary key for Church; referenced by related tables.
from_schema: https://global.church/schema
rank: 1000
identifier: true
alias: church_id
domain_of:
- Church
range: uuid
required: true

```
</details>