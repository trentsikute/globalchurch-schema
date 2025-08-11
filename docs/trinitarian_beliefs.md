

# Slot: trinitarian_beliefs 


_Whether the church affirms classical Trinitarian doctrine._





URI: [gc:trinitarian_beliefs](https://global.church/schema/trinitarian_beliefs)
Alias: trinitarian_beliefs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnrichedData](EnrichedData.md) | AI-enriched attributes extracted from the church website and socials |  no  |






## Properties

* Range: [Boolean](Boolean.md)





## Examples

| Value |
| --- |
| true |
| false |

## Comments

* Boolean derived from site language (e.g., statements referencing Father, Son, Holy Spirit).
When unknown or ambiguous, leave unset rather than guessing.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:trinitarian_beliefs |
| native | gc:trinitarian_beliefs |




## LinkML Source

<details>
```yaml
name: trinitarian_beliefs
description: Whether the church affirms classical Trinitarian doctrine.
comments:
- 'Boolean derived from site language (e.g., statements referencing Father, Son, Holy
  Spirit).

  When unknown or ambiguous, leave unset rather than guessing.

  '
examples:
- value: 'true'
  description: Affirmed on the Beliefs page.
- value: 'false'
  description: Explicitly non-Trinitarian statement.
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
rank: 1000
alias: trinitarian_beliefs
domain_of:
- EnrichedData
range: boolean

```
</details>