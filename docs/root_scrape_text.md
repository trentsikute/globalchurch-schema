

# Slot: root_scrape_text 


_Visible text content scraped from the website root page._





URI: [gc:root_scrape_text](https://global.church/schema/root_scrape_text)
Alias: root_scrape_text

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
| Welcome to Grace Community Church! Join us Sundays at 9am and 11am. Our mission is to serve Malibu and beyond... |

## Comments

* The full visible text extracted from the HTML body of the root URL of the church website.
Used for downstream enrichment, NLP, and data extraction.
Not intended for public display; may contain headers, footers, and navigation text.
For structured content, see other enrichment slots.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:root_scrape_text |
| native | gc:root_scrape_text |




## LinkML Source

<details>
```yaml
name: root_scrape_text
description: Visible text content scraped from the website root page.
comments:
- 'The full visible text extracted from the HTML body of the root URL of the church
  website.

  Used for downstream enrichment, NLP, and data extraction.

  Not intended for public display; may contain headers, footers, and navigation text.

  For structured content, see other enrichment slots.

  '
examples:
- value: Welcome to Grace Community Church! Join us Sundays at 9am and 11am. Our mission
    is to serve Malibu and beyond...
  description: Scraped homepage text sample.
in_subset:
- internal
from_schema: https://global.church/schema
rank: 1000
alias: root_scrape_text
domain_of:
- ChurchWebsite
range: string

```
</details>