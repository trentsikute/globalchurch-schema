

# Slot: root_scrape_check 


_Checksum or status flag indicating scrape state._





URI: [gc:root_scrape_check](https://global.church/schema/root_scrape_check)
Alias: root_scrape_check

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChurchWebsite](ChurchWebsite.md) | Raw scrape artifacts captured from the church root URL |  no  |






## Properties

* Range: [String](String.md)





## Examples

| Value |
| --- |
| sha256:3b2d9f3a… |
| timeout |

## Comments

* Use for lightweight integrity checks (e.g., a hash of the DOM or a status string
like “ok”, “blocked”, “timeout”). Helps detect page changes between scrapes.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:root_scrape_check |
| native | gc:root_scrape_check |




## LinkML Source

<details>
```yaml
name: root_scrape_check
description: Checksum or status flag indicating scrape state.
comments:
- 'Use for lightweight integrity checks (e.g., a hash of the DOM or a status string

  like “ok”, “blocked”, “timeout”). Helps detect page changes between scrapes.

  '
examples:
- value: sha256:3b2d9f3a…
  description: Digest of the normalized page content.
- value: timeout
  description: Network timeout recorded during scraping.
in_subset:
- internal
from_schema: https://global.church/schema
rank: 1000
alias: root_scrape_check
domain_of:
- ChurchWebsite
range: string

```
</details>