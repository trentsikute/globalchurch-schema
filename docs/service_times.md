

# Slot: service_times 


_Service times (free text)._





URI: [gc:service_times](https://global.church/schema/service_times)
Alias: service_times

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
| self | gc:service_times |
| native | gc:service_times |




## LinkML Source

<details>
```yaml
name: service_times
description: Service times (free text).
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
rank: 1000
alias: service_times
domain_of:
- EnrichedData
range: string

```
</details>