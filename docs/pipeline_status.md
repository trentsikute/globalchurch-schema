

# Slot: pipeline_status 


_Current enrichment pipeline stage._





URI: [gc:pipeline_status](https://global.church/schema/pipeline_status)
Alias: pipeline_status

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
| RAW |
| VALIDATED |

## Comments

* Suggested stages: RAW → CLEAN → ENRICHED → VALIDATED.
RAW: ingested with minimal checks.
CLEAN: deduplicated & normalized.
ENRICHED: scraped/AI fields added.
VALIDATED: human-reviewed.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:pipeline_status |
| native | gc:pipeline_status |




## LinkML Source

<details>
```yaml
name: pipeline_status
description: Current enrichment pipeline stage.
comments:
- 'Suggested stages: RAW → CLEAN → ENRICHED → VALIDATED.

  RAW: ingested with minimal checks.

  CLEAN: deduplicated & normalized.

  ENRICHED: scraped/AI fields added.

  VALIDATED: human-reviewed.

  '
examples:
- value: RAW
  description: Fresh intake from a seed source.
- value: VALIDATED
  description: Reviewed and approved record.
in_subset:
- internal
from_schema: https://global.church/schema
rank: 1000
alias: pipeline_status
domain_of:
- Church
range: string

```
</details>