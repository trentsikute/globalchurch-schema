

# Slot: service_languages 


_Languages in which services are offered._





URI: [gc:service_languages](https://global.church/schema/service_languages)
Alias: service_languages

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
| self | gc:service_languages |
| native | gc:service_languages |
| exact | schema:inLanguage |




## LinkML Source

<details>
```yaml
name: service_languages
description: Languages in which services are offered.
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
exact_mappings:
- schema:inLanguage
rank: 1000
alias: service_languages
domain_of:
- EnrichedData
range: string

```
</details>