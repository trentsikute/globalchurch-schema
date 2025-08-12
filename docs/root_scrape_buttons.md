

# Slot: root_scrape_buttons 


_Button texts captured on the root page._





URI: [gc:root_scrape_buttons](https://global.church/schema/root_scrape_buttons)
Alias: root_scrape_buttons

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChurchWebsiteText](ChurchWebsiteText.md) | Raw scrape artifacts captured from the church root URL |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| ["Plan a Visit", "Watch Live", "Give"] |

## Comments

* Capture the visible labels of clickable buttons/links from the root URL
(e.g., “Plan a Visit”, “Give”, “Watch Live”). Useful for enrichment heuristics.
This is raw scrape output and may include navigation or repeated items.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:root_scrape_buttons |
| native | gc:root_scrape_buttons |




## LinkML Source

<details>
```yaml
name: root_scrape_buttons
description: Button texts captured on the root page.
comments:
- 'Capture the visible labels of clickable buttons/links from the root URL

  (e.g., “Plan a Visit”, “Give”, “Watch Live”). Useful for enrichment heuristics.

  This is raw scrape output and may include navigation or repeated items.

  '
examples:
- value: '["Plan a Visit", "Watch Live", "Give"]'
  description: Common calls-to-action from a church homepage as a JSON array string.
in_subset:
- internal
from_schema: https://global.church/schema
rank: 1000
alias: root_scrape_buttons
domain_of:
- ChurchWebsiteText
range: string

```
</details>