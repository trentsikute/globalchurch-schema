

# Slot: youtube_url 


_YouTube channel URL._





URI: [gc:youtube_url](https://global.church/schema/youtube_url)
Alias: youtube_url

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnrichedData](EnrichedData.md) | AI-enriched attributes extracted from the church website and socials |  no  |






## Properties

* Range: [Uri](Uri.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:youtube_url |
| native | gc:youtube_url |
| exact | schema:sameAs |




## LinkML Source

<details>
```yaml
name: youtube_url
description: YouTube channel URL.
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
exact_mappings:
- schema:sameAs
rank: 1000
alias: youtube_url
domain_of:
- EnrichedData
range: uri

```
</details>