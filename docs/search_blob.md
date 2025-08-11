

# Slot: search_blob 


_Concatenated text of searchable fields for indexing._





URI: [gc:search_blob](https://global.church/schema/search_blob)
Alias: search_blob

<!-- no inheritance hierarchy -->







## Properties

* Range: [String](String.md)





## Examples

| Value |
| --- |
| Grace Community Church 123 Main St Springfield CA 62704 US |

## Comments

* This slot is used internally to store a combined string of key fields
(e.g., name, address, keywords) for full-text search indexing.
Not intended for direct display or export.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:search_blob |
| native | gc:search_blob |




## LinkML Source

<details>
```yaml
name: search_blob
description: Concatenated text of searchable fields for indexing.
comments:
- 'This slot is used internally to store a combined string of key fields

  (e.g., name, address, keywords) for full-text search indexing.

  Not intended for direct display or export.

  '
examples:
- value: Grace Community Church 123 Main St Springfield CA 62704 US
  description: Combined fields for search.
in_subset:
- internal
from_schema: https://global.church/schema
rank: 1000
alias: search_blob
range: string

```
</details>