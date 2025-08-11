

# Slot: name 


_Official church name._





URI: [gc:name](https://global.church/schema/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  yes  |






## Properties

* Range: [String](String.md)





## Examples

| Value |
| --- |
| Grace Community Church |
| Grace Church Malibu |

## Comments

* Use the legal or commonly recognized name (e.g., “Grace Community Church”).
If there is a campus name or colloquial short name, store it in `alternate_name`.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:name |
| native | gc:name |
| exact | schema:name |




## LinkML Source

<details>
```yaml
name: name
description: Official church name.
comments:
- 'Use the legal or commonly recognized name (e.g., “Grace Community Church”).

  If there is a campus name or colloquial short name, store it in `alternate_name`.

  '
examples:
- value: Grace Community Church
  description: Formal church name.
- value: Grace Church Malibu
  description: Name with locality qualifier.
in_subset:
- church_core
- public
from_schema: https://global.church/schema
exact_mappings:
- schema:name
rank: 1000
alias: name
domain_of:
- Church
range: string

```
</details>