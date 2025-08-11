

# Slot: scraped_email 


_Email address extracted from site._





URI: [gc:scraped_email](https://global.church/schema/scraped_email)
Alias: scraped_email

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnrichedData](EnrichedData.md) | AI-enriched attributes extracted from the church website and socials |  no  |






## Properties

* Range: [email](email.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:scraped_email |
| native | gc:scraped_email |
| exact | schema:email |




## LinkML Source

<details>
```yaml
name: scraped_email
description: Email address extracted from site.
in_subset:
- internal
- pii
- enrichment
from_schema: https://global.church/schema
exact_mappings:
- schema:email
rank: 1000
alias: scraped_email
domain_of:
- EnrichedData
range: email

```
</details>