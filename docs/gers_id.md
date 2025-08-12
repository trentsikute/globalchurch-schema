

# Slot: gers_id 


_Government/Ecclesiastical Registry System identifier._





URI: [gc:gers_id](https://global.church/schema/gers_id)
Alias: gers_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Overture](Overture.md) | Original place record as supplied by Overture Maps |  no  |
| [Church](Church.md) | A distinct church congregation |  no  |







## Properties

* Range: [String](String.md)

* Required: True






## Examples

| Value |
| --- |
| GERS-CA-00012345 |

## Comments

* External registry identifier used for cross-referencing with official listings.
May not exist for all churches.


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
description: Government/Ecclesiastical Registry System identifier.
comments:
- 'External registry identifier used for cross-referencing with official listings.

  May not exist for all churches.

  '
examples:
- value: GERS-CA-00012345
  description: Sample registry ID.
in_subset:
- overture
- public
from_schema: https://global.church/schema
rank: 1000
identifier: true
alias: gers_id
domain_of:
- Church
- Overture
range: string
required: true

```
</details>