

# Slot: programs_offered 


_List of programs or ministries offered._





URI: [gc:programs_offered](https://global.church/schema/programs_offered)
Alias: programs_offered

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnrichedData](EnrichedData.md) | AI-enriched attributes extracted from the church website and socials |  no  |






## Properties

* Range: [String](String.md)




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
description: List of programs or ministries offered.
from_schema: https://global.church/schema
exact_mappings:
- schema:service
rank: 1000
alias: programs_offered
domain_of:
- EnrichedData
range: string

```
</details>