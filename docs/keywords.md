

# Slot: keywords 


_Keywords or tags describing the church._





URI: [gc:keywords](https://global.church/schema/keywords)
Alias: keywords

<!-- no inheritance hierarchy -->







## Properties

* Range: [String](String.md)

* Multivalued: True





## Examples

| Value |
| --- |
| ["baptist", "youth", "outreach"] |

## Comments

* NOTE: It has not yet been decided what values (if any) will be used in this slot.
This field was added because it matches the schema.org schema.

Comma-separated or list of keywords that describe the church, its ministries, or focus areas.
Use consistent tagging to enable filtering and search.
Examples: "baptist, youth, outreach, contemporary worship"


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:keywords |
| native | gc:keywords |
| exact | schema:keywords |




## LinkML Source

<details>
```yaml
name: keywords
description: Keywords or tags describing the church.
comments:
- 'NOTE: It has not yet been decided what values (if any) will be used in this slot.

  This field was added because it matches the schema.org schema.


  Comma-separated or list of keywords that describe the church, its ministries, or
  focus areas.

  Use consistent tagging to enable filtering and search.

  Examples: "baptist, youth, outreach, contemporary worship"

  '
examples:
- value: '["baptist", "youth", "outreach"]'
  description: Multiple ministry keywords.
in_subset:
- public
from_schema: https://global.church/schema
exact_mappings:
- schema:keywords
rank: 1000
alias: keywords
range: string
multivalued: true

```
</details>