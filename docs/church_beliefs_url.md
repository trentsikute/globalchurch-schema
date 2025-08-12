

# Slot: church_beliefs_url 


_URL for the church’s statement of beliefs/faith._





URI: [gc:church_beliefs_url](https://global.church/schema/church_beliefs_url)
Alias: church_beliefs_url

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  no  |







## Properties

* Range: [Uri](Uri.md)






## Examples

| Value |
| --- |
| https://gracechurch.org/beliefs |

## Comments

* Prefer the canonical “Beliefs” page for doctrinal summaries.
If multiple pages exist, choose the most comprehensive source.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:church_beliefs_url |
| native | gc:church_beliefs_url |




## LinkML Source

<details>
```yaml
name: church_beliefs_url
description: URL for the church’s statement of beliefs/faith.
comments:
- 'Prefer the canonical “Beliefs” page for doctrinal summaries.

  If multiple pages exist, choose the most comprehensive source.

  '
examples:
- value: https://gracechurch.org/beliefs
  description: Canonical beliefs page.
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
rank: 1000
alias: church_beliefs_url
domain_of:
- Church
range: uri

```
</details>