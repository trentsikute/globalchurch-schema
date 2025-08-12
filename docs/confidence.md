

# Slot: confidence 


_Confidence score (0–1) from Overture._





URI: [gc:confidence](https://global.church/schema/confidence)
Alias: confidence

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Overture](Overture.md) | Original place record as supplied by Overture Maps |  no  |







## Properties

* Range: [Float](Float.md)






## Examples

| Value |
| --- |
| 0.92 |

## Comments

* A numeric score indicating confidence in the match or attribution.
If absent upstream, leave empty rather than inventing a value.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:confidence |
| native | gc:confidence |




## LinkML Source

<details>
```yaml
name: confidence
description: Confidence score (0–1) from Overture.
comments:
- 'A numeric score indicating confidence in the match or attribution.

  If absent upstream, leave empty rather than inventing a value.

  '
examples:
- value: '0.92'
  description: High-confidence attribution.
in_subset:
- overture
from_schema: https://global.church/schema
rank: 1000
alias: confidence
domain_of:
- Overture
range: float

```
</details>