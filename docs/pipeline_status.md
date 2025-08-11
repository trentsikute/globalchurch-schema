

# Slot: pipeline_status 


_Enrichment pipeline stage (e.g., RAW, CLEAN, ENRICHED, VALIDATED)._





URI: [gc:pipeline_status](https://global.church/schema/pipeline_status)
Alias: pipeline_status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  no  |






## Properties

* Range: [String](String.md)




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
description: Enrichment pipeline stage (e.g., RAW, CLEAN, ENRICHED, VALIDATED).
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