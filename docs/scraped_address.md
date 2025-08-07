

# Slot: scraped_address 


_Postal address extracted from site._





URI: [gc:scraped_address](https://global.church/schema/scraped_address)
Alias: scraped_address

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
| self | gc:scraped_address |
| native | gc:scraped_address |
| exact | schema:address |




## LinkML Source

<details>
```yaml
name: scraped_address
description: Postal address extracted from site.
from_schema: https://global.church/schema
exact_mappings:
- schema:address
rank: 1000
alias: scraped_address
domain_of:
- EnrichedData
range: string

```
</details>