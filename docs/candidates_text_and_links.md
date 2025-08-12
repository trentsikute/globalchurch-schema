

# Slot: candidates_text_and_links 


_Text snippets and associated links for candidate pages._





URI: [gc:candidates_text_and_links](https://global.church/schema/candidates_text_and_links)
Alias: candidates_text_and_links

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChurchWebsiteText](ChurchWebsiteText.md) | Raw scrape artifacts captured from the church root URL |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| ["{\"text\": \"Beliefs\", \"url\": \"https://gracechurch.org/beliefs\"}", "{\"text\": \"Plan a Visit\", \"url\": \"https://gracechurch.org/visit\"}"] |

## Comments

* Use a consistent representation (e.g., JSON strings) pairing anchor text with href.
Example object shape: {"text": "Beliefs", "url": "https://…/beliefs"}.
Helps prioritize which candidate links are most relevant.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:candidates_text_and_links |
| native | gc:candidates_text_and_links |




## LinkML Source

<details>
```yaml
name: candidates_text_and_links
description: Text snippets and associated links for candidate pages.
comments:
- 'Use a consistent representation (e.g., JSON strings) pairing anchor text with href.

  Example object shape: {"text": "Beliefs", "url": "https://…/beliefs"}.

  Helps prioritize which candidate links are most relevant.

  '
examples:
- value: '["{\"text\": \"Beliefs\", \"url\": \"https://gracechurch.org/beliefs\"}",
    "{\"text\": \"Plan a Visit\", \"url\": \"https://gracechurch.org/visit\"}"]'
  description: Two text–link pairs serialized as a JSON array of JSON objects.
in_subset:
- internal
from_schema: https://global.church/schema
rank: 1000
alias: candidates_text_and_links
domain_of:
- ChurchWebsiteText
range: string
multivalued: true

```
</details>