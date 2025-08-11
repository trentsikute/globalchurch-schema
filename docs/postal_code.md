

# Slot: postal_code 


_Postal code or ZIP code for the address._





URI: [gc:postal_code](https://global.church/schema/postal_code)
Alias: postal_code

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  no  |






## Properties

* Range: [String](String.md)





## Examples

| Value |
| --- |
| 62704 |
| SW1A 2AA |

## Comments

* The postal (ZIP) code as assigned by the national postal authority.
Use the correct format for the country (e.g., 12345 or 12345-6789 in the US, SW1A 2AA in the UK).
Always include this value for postal addresses if available.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:postal_code |
| native | gc:postal_code |
| exact | schema:postalCode |




## LinkML Source

<details>
```yaml
name: postal_code
description: Postal code or ZIP code for the address.
comments:
- 'The postal (ZIP) code as assigned by the national postal authority.

  Use the correct format for the country (e.g., 12345 or 12345-6789 in the US, SW1A
  2AA in the UK).

  Always include this value for postal addresses if available.

  '
examples:
- value: '62704'
  description: US ZIP code.
- value: SW1A 2AA
  description: UK postal code.
in_subset:
- church_core
- public
from_schema: https://global.church/schema
exact_mappings:
- schema:postalCode
rank: 1000
alias: postal_code
domain_of:
- Church
range: string

```
</details>