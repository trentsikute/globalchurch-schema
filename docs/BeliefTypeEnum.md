# Enum: BeliefTypeEnum 




_Top-level Christian family grouping used by Global.Church. Based on Harvest Information Standards (HIS) Registry of Religions. https://hisregistries.org/ror/_



URI: [BeliefTypeEnum](BeliefTypeEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| orthodox | None | Eastern Orthodox and Oriental Orthodox churches |
| roman_catholic | None | Roman Catholic Church |
| protestant | None | Protestant denominations |
| anglican | None | Anglican Communion and related churches |
| other | None | Any other Trinitarian Christian tradition not listed above |
| unknown | None | Belief type has not been determined |




## Slots

| Name | Description |
| ---  | --- |
| [belief_type](belief_type.md) | Denomination / church type category |






## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema






## LinkML Source

<details>
```yaml
name: BeliefTypeEnum
description: Top-level Christian family grouping used by Global.Church. Based on Harvest
  Information Standards (HIS) Registry of Religions. https://hisregistries.org/ror/
from_schema: https://global.church/schema
rank: 1000
permissible_values:
  orthodox:
    text: orthodox
    description: Eastern Orthodox and Oriental Orthodox churches.
    aliases:
    - Orthodox
  roman_catholic:
    text: roman_catholic
    description: Roman Catholic Church.
    aliases:
    - Roman Catholic
  protestant:
    text: protestant
    description: Protestant denominations.
    aliases:
    - Protestant
  anglican:
    text: anglican
    description: Anglican Communion and related churches.
    aliases:
    - Anglican
  other:
    text: other
    description: Any other Trinitarian Christian tradition not listed above. Similar
      to 'Independent' in HIS.
    aliases:
    - Other
  unknown:
    text: unknown
    description: Belief type has not been determined.
    aliases:
    - Unknown

```
</details>
