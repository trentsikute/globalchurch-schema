

# Slot: gers_id 


_ID from the Government/Ecclesiastical Registry System (if available)._





URI: [gc:gers_id](https://global.church/schema/gers_id)
Alias: gers_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  no  |
| [Overture](Overture.md) | Original place record as supplied by Overture Maps |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:gers_id |
| native | gc:gers_id |




## LinkML Source

<details>
```yaml
name: gers_id
description: ID from the Government/Ecclesiastical Registry System (if available).
in_subset:
- overture
- public
from_schema: https://global.church/schema
rank: 1000
alias: gers_id
domain_of:
- Church
- Overture
range: string

```
</details>