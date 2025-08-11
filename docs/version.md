

# Slot: version 


_Overture dataset version number._





URI: [gc:version](https://global.church/schema/version)
Alias: version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Overture](Overture.md) | Original place record as supplied by Overture Maps |  no  |






## Properties

* Range: [Integer](Integer.md)





## Examples

| Value |
| --- |
| 13 |

## Comments

* Integer version tag from the Overture Maps release metadata.
Use with `source_release` when available.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:version |
| native | gc:version |




## LinkML Source

<details>
```yaml
name: version
description: Overture dataset version number.
comments:
- 'Integer version tag from the Overture Maps release metadata.

  Use with `source_release` when available.

  '
examples:
- value: '13'
  description: Example Overture version.
in_subset:
- overture
from_schema: https://global.church/schema
rank: 1000
alias: version
domain_of:
- Overture
range: integer

```
</details>