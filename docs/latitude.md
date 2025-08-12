

# Slot: latitude 


_Latitude in decimal degrees._





URI: [gc:latitude](https://global.church/schema/latitude)
Alias: latitude

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  yes  |







## Properties

* Range: [Float](Float.md)

* Minimum Value: -90

* Maximum Value: 90






## Examples

| Value |
| --- |
| 34.0259 |
| -33.8688 |

## Comments

* Use WGS84 decimal degrees. South is negative.
Precision of 5–6 decimal places is typically sufficient (~1–10 meters).


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:latitude |
| native | gc:latitude |
| exact | schema:latitude |




## LinkML Source

<details>
```yaml
name: latitude
description: Latitude in decimal degrees.
comments:
- 'Use WGS84 decimal degrees. South is negative.

  Precision of 5–6 decimal places is typically sufficient (~1–10 meters).

  '
examples:
- value: '34.0259'
  description: Approximate latitude for Malibu, CA.
- value: '-33.8688'
  description: Southern hemisphere example (Sydney).
in_subset:
- church_core
- public
from_schema: https://global.church/schema
exact_mappings:
- schema:latitude
rank: 1000
alias: latitude
domain_of:
- Church
range: float
minimum_value: -90
maximum_value: 90

```
</details>