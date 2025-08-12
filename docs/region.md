

# Slot: region 


_State, province, or administrative region._





URI: [gc:region](https://global.church/schema/region)
Alias: region

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| CA |
| New South Wales |

## Comments

* The primary administrative subdivision for the locality, such as state (US), province (Canada), or region (EU).
Use the full name or standard abbreviation as appropriate for the country.
For countries without such subdivisions, leave this slot empty.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:region |
| native | gc:region |
| exact | schema:addressRegion |




## LinkML Source

<details>
```yaml
name: region
description: State, province, or administrative region.
comments:
- 'The primary administrative subdivision for the locality, such as state (US), province
  (Canada), or region (EU).

  Use the full name or standard abbreviation as appropriate for the country.

  For countries without such subdivisions, leave this slot empty.

  '
examples:
- value: CA
  description: California (US state abbreviation).
- value: New South Wales
  description: Australian state.
in_subset:
- church_core
- public
from_schema: https://global.church/schema
exact_mappings:
- schema:addressRegion
rank: 1000
alias: region
domain_of:
- Church
range: string

```
</details>