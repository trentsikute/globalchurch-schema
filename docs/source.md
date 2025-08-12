

# Slot: source 


_Source label from Overture Maps._





URI: [gc:source](https://global.church/schema/source)
Alias: source

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Overture](Overture.md) | Original place record as supplied by Overture Maps |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| overture_places |

## Comments

* The upstream source name (e.g., “overture_places”, “overture_poi”).
Helps with lineage and debugging.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:source |
| native | gc:source |




## LinkML Source

<details>
```yaml
name: source
description: Source label from Overture Maps.
comments:
- 'The upstream source name (e.g., “overture_places”, “overture_poi”).

  Helps with lineage and debugging.

  '
examples:
- value: overture_places
  description: Upstream dataset label.
in_subset:
- overture
from_schema: https://global.church/schema
rank: 1000
alias: source
domain_of:
- Overture
range: string

```
</details>