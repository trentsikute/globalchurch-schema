

# Slot: locality 


_City or locality where the church is located._





URI: [gc:locality](https://global.church/schema/locality)
Alias: locality

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  no  |






## Properties

* Range: [String](String.md)





## Examples

| Value |
| --- |
| Springfield |
| Sydney |

## Comments

* The city, town, or locality where the church's primary address is situated.
Use the official or most commonly recognized municipality name.
This value should match the locality as used by local postal authorities.
For rural areas without a city, use the nearest recognized locality.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:locality |
| native | gc:locality |
| exact | schema:addressLocality |




## LinkML Source

<details>
```yaml
name: locality
description: City or locality where the church is located.
comments:
- 'The city, town, or locality where the church''s primary address is situated.

  Use the official or most commonly recognized municipality name.

  This value should match the locality as used by local postal authorities.

  For rural areas without a city, use the nearest recognized locality.

  '
examples:
- value: Springfield
  description: US city.
- value: Sydney
  description: Major city in Australia.
in_subset:
- church_core
- public
from_schema: https://global.church/schema
exact_mappings:
- schema:addressLocality
rank: 1000
alias: locality
domain_of:
- Church
range: string

```
</details>