

# Slot: church_id 


_Global.Church-issued ID for a church._





URI: [gc:church_id](https://global.church/schema/church_id)
Alias: church_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnrichedData](EnrichedData.md) | AI-enriched attributes extracted from the church website and socials |  no  |
| [ChurchWebsite](ChurchWebsite.md) | Raw scrape artifacts captured from the church root URL |  no  |
| [Church](Church.md) | A distinct church congregation |  yes  |






## Properties

* Range: [Uuid](Uuid.md)

* Required: True





## Examples

| Value |
| --- |
| 9e1c2a7d-4c33-4b8b-9d7a-1a2b3c4d5e6f |

## Comments

* Primary key for the Church entity. Stable and non-reassignable.
Used as the foreign key for ChurchWebsite, EnrichedData, and other related records.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:church_id |
| native | gc:church_id |




## LinkML Source

<details>
```yaml
name: church_id
description: Global.Church-issued ID for a church.
comments:
- 'Primary key for the Church entity. Stable and non-reassignable.

  Used as the foreign key for ChurchWebsite, EnrichedData, and other related records.

  '
examples:
- value: 9e1c2a7d-4c33-4b8b-9d7a-1a2b3c4d5e6f
  description: Example church UUID.
in_subset:
- church_core
- public
from_schema: https://global.church/schema
rank: 1000
identifier: true
alias: church_id
domain_of:
- Church
- ChurchWebsite
- EnrichedData
range: uuid
required: true

```
</details>