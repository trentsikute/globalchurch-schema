

# Slot: root_candidates 


_Candidate URLs extracted from the root page._





URI: [gc:root_candidates](https://global.church/schema/root_candidates)
Alias: root_candidates

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChurchWebsite](ChurchWebsite.md) | Raw scrape artifacts captured from the church root URL |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True





## Examples

| Value |
| --- |
| ["https://gracechurch.org/beliefs", "https://gracechurch.org/ministries"] |

## Comments

* Potential internal links to pages like “Beliefs”, “Ministries”, “Visit”, etc.
Feed these into downstream enrichment for targeted scraping.
Store fully qualified URLs when possible.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:root_candidates |
| native | gc:root_candidates |




## LinkML Source

<details>
```yaml
name: root_candidates
description: Candidate URLs extracted from the root page.
comments:
- 'Potential internal links to pages like “Beliefs”, “Ministries”, “Visit”, etc.

  Feed these into downstream enrichment for targeted scraping.

  Store fully qualified URLs when possible.

  '
examples:
- value: '["https://gracechurch.org/beliefs", "https://gracechurch.org/ministries"]'
  description: Two high-value candidate pages as a JSON array string.
in_subset:
- internal
from_schema: https://global.church/schema
rank: 1000
alias: root_candidates
domain_of:
- ChurchWebsite
range: string
multivalued: true

```
</details>