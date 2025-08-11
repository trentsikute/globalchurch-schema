

# Slot: programs_offered 


_Programs or ministries the church offers._





URI: [gc:programs_offered](https://global.church/schema/programs_offered)
Alias: programs_offered

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnrichedData](EnrichedData.md) | AI-enriched attributes extracted from the church website and socials |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True





## Examples

| Value |
| --- |
| ["Youth Ministry", "Food Pantry", "Alpha Course"] |

## Comments

* List distinct program names (e.g., “Youth”, “Alpha”, “Food Pantry”).
Prefer stable, human-readable labels; avoid internal codes in public data.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:programs_offered |
| native | gc:programs_offered |
| exact | schema:service |




## LinkML Source

<details>
```yaml
name: programs_offered
description: Programs or ministries the church offers.
comments:
- 'List distinct program names (e.g., “Youth”, “Alpha”, “Food Pantry”).

  Prefer stable, human-readable labels; avoid internal codes in public data.

  '
examples:
- value: '["Youth Ministry", "Food Pantry", "Alpha Course"]'
  description: Three public-facing programs as a JSON array string.
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
exact_mappings:
- schema:service
rank: 1000
alias: programs_offered
domain_of:
- EnrichedData
range: string
multivalued: true

```
</details>