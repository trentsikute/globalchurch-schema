

# Slot: website 


_Full website URL for the church._





URI: [gc:website](https://global.church/schema/website)
Alias: website

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
| https://gracechurch.org |
| https://stpauls-sydney.org.au |

## Comments

* Provide the complete URL, including scheme (http/https).
Use the main public-facing website for the church.
Exclude social media links (see `instagram_url`, `youtube_url`).


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:website |
| native | gc:website |
| exact | schema:url |




## LinkML Source

<details>
```yaml
name: website
description: Full website URL for the church.
comments:
- 'Provide the complete URL, including scheme (http/https).

  Use the main public-facing website for the church.

  Exclude social media links (see `instagram_url`, `youtube_url`).

  '
examples:
- value: https://gracechurch.org
  description: Church homepage.
- value: https://stpauls-sydney.org.au
  description: Australian church website.
in_subset:
- public
from_schema: https://global.church/schema
exact_mappings:
- schema:url
rank: 1000
alias: website
domain_of:
- Church
range: uri

```
</details>