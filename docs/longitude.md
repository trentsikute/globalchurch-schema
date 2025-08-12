

# Slot: longitude 


_Longitude in decimal degrees._





URI: [gc:longitude](https://global.church/schema/longitude)
Alias: longitude

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  yes  |







## Properties

* Range: [Float](Float.md)

* Minimum Value: -180

* Maximum Value: 180






## Examples

| Value |
| --- |
| -118.7798 |
| 151.2093 |

## Comments

* Use WGS84 decimal degrees. West is negative.
Keep latitude/longitude pairs from the same source to avoid mismatch.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:longitude |
| native | gc:longitude |
| exact | schema:longitude |




## LinkML Source

<details>
```yaml
name: longitude
description: Longitude in decimal degrees.
comments:
- 'Use WGS84 decimal degrees. West is negative.

  Keep latitude/longitude pairs from the same source to avoid mismatch.

  '
examples:
- value: '-118.7798'
  description: Approximate longitude for Malibu, CA.
- value: '151.2093'
  description: Eastern hemisphere example (Sydney).
in_subset:
- church_core
- public
from_schema: https://global.church/schema
exact_mappings:
- schema:longitude
rank: 1000
alias: longitude
domain_of:
- Church
range: float
minimum_value: -180
maximum_value: 180

```
</details>