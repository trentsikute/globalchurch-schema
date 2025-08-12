

# Slot: belief_type 


_Denomination / church type category._

_Classifies the church into a top-level Christian family as defined by BeliefTypeEnum._

_Based on the Harvest Information Standards (HIS) Registry of Religions._

__





URI: [gc:belief_type](https://global.church/schema/belief_type)
Alias: belief_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  no  |







## Properties

* Range: [BeliefTypeEnum](BeliefTypeEnum.md)






## Examples

| Value |
| --- |
| protestant |
| unknown |

## Comments

* Use the controlled values in BeliefTypeEnum. When unclear, set `unknown`.
You may revise this after human review.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:belief_type |
| native | gc:belief_type |




## LinkML Source

<details>
```yaml
name: belief_type
description: 'Denomination / church type category.

  Classifies the church into a top-level Christian family as defined by BeliefTypeEnum.

  Based on the Harvest Information Standards (HIS) Registry of Religions.

  '
comments:
- 'Use the controlled values in BeliefTypeEnum. When unclear, set `unknown`.

  You may revise this after human review.

  '
examples:
- value: protestant
  description: Derived from the site’s denomination statement.
- value: unknown
  description: Insufficient info to classify.
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
rank: 1000
alias: belief_type
domain_of:
- Church
range: BeliefTypeEnum

```
</details>