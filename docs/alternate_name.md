

# Slot: alternate_name 


_Alternate, colloquial, or short name for the church._





URI: [gc:alternate_name](https://global.church/schema/alternate_name)
Alias: alternate_name

<!-- no inheritance hierarchy -->







## Properties

* Range: [String](String.md)





## Examples

| Value |
| --- |
| Grace Church |
| GCC Malibu |

## Comments

* Use for commonly used nicknames, abbreviations, or campus-specific names.
Leave blank if the church is only known by its official name.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:alternate_name |
| native | gc:alternate_name |
| exact | schema:alternateName |




## LinkML Source

<details>
```yaml
name: alternate_name
description: Alternate, colloquial, or short name for the church.
comments:
- 'Use for commonly used nicknames, abbreviations, or campus-specific names.

  Leave blank if the church is only known by its official name.

  '
examples:
- value: Grace Church
  description: Shortened version of official name.
- value: GCC Malibu
  description: Colloquial campus name.
in_subset:
- public
from_schema: https://global.church/schema
exact_mappings:
- schema:alternateName
rank: 1000
alias: alternate_name
range: string

```
</details>