

# Slot: belief_type 


_Denomination / church type category.  _

_This slot classifies a church into one of several top-level Christian family groupings_

_as defined by the BeliefTypeEnum.  _

_Based on the Harvest Information Standards (HIS) Registry of Religions._

__





URI: [gc:belief_type](https://global.church/schema/belief_type)
Alias: belief_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnrichedData](EnrichedData.md) | AI-enriched attributes extracted from the church website and socials |  no  |






## Properties

* Range: [BeliefTypeEnum](BeliefTypeEnum.md)




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
description: "Denomination / church type category.  \nThis slot classifies a church\
  \ into one of several top-level Christian family groupings\nas defined by the BeliefTypeEnum.\
  \  \nBased on the Harvest Information Standards (HIS) Registry of Religions.\n"
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
rank: 1000
alias: belief_type
domain_of:
- EnrichedData
range: BeliefTypeEnum

```
</details>