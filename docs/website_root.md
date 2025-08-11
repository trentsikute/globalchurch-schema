

# Slot: website_root 


_Root URL of the church website (scheme and domain only)._





URI: [gc:website_root](https://global.church/schema/website_root)
Alias: website_root

<!-- no inheritance hierarchy -->







## Properties

* Range: [Uri](Uri.md)





## Examples

| Value |
| --- |
| https://gracechurch.org |
| https://stpauls-sydney.org.au |

## Comments

* The canonical root domain for the church website, e.g., https://example.org.
Used for web scraping and deduplication.
Exclude any path, query, or fragment components.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:website_root |
| native | gc:website_root |




## LinkML Source

<details>
```yaml
name: website_root
description: Root URL of the church website (scheme and domain only).
comments:
- 'The canonical root domain for the church website, e.g., https://example.org.

  Used for web scraping and deduplication.

  Exclude any path, query, or fragment components.

  '
examples:
- value: https://gracechurch.org
  description: Root domain for scraping.
- value: https://stpauls-sydney.org.au
  description: Australian church root domain.
in_subset:
- internal
from_schema: https://global.church/schema
rank: 1000
alias: website_root
range: uri

```
</details>