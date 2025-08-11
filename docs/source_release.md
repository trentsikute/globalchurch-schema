

# Slot: source_release 


_Overture release tag (YYYY-MM-DD)._





URI: [gc:source_release](https://global.church/schema/source_release)
Alias: source_release

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Overture](Overture.md) | Original place record as supplied by Overture Maps |  no  |






## Properties

* Range: [String](String.md)





## Examples

| Value |
| --- |
| 2024-05-15 |

## Comments

* The official release date string from Overture (e.g., 2024-05-15).
Use ISO 8601 date format.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:source_release |
| native | gc:source_release |




## LinkML Source

<details>
```yaml
name: source_release
description: Overture release tag (YYYY-MM-DD).
comments:
- 'The official release date string from Overture (e.g., 2024-05-15).

  Use ISO 8601 date format.

  '
examples:
- value: '2024-05-15'
  description: Release date.
in_subset:
- overture
from_schema: https://global.church/schema
rank: 1000
alias: source_release
domain_of:
- Overture
range: string

```
</details>