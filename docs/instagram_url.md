

# Slot: instagram_url 


_Instagram profile URL._





URI: [gc:instagram_url](https://global.church/schema/instagram_url)
Alias: instagram_url

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
| https://www.instagram.com/gracechurch/ |

## Comments

* Prefer the canonical profile (not a hashtag or location page).
Normalize to the https scheme.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:instagram_url |
| native | gc:instagram_url |
| exact | schema:sameAs |




## LinkML Source

<details>
```yaml
name: instagram_url
description: Instagram profile URL.
comments:
- 'Prefer the canonical profile (not a hashtag or location page).

  Normalize to the https scheme.

  '
examples:
- value: https://www.instagram.com/gracechurch/
  description: Canonical Instagram URL.
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
exact_mappings:
- schema:sameAs
rank: 1000
alias: instagram_url
domain_of:
- Church
range: uri

```
</details>