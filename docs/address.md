

# Slot: address 


_Physical street address of the church or user._





URI: [gc:address](https://global.church/schema/address)
Alias: address

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
| 123 Main St, Springfield, IL 62704 |
| 10 Downing St, London SW1A 2AA |

## Comments

* This is the official mailing or street address, suitable for postal delivery and mapping.
Always include street number, street name, and any suite or apartment details if applicable.
Follow the local postal format for the country (e.g., street before city in the US).
Avoid using P.O. boxes unless it is the only available mailing address for the entity.
For international addresses, include all relevant locality and region information.
Use this slot for the canonical address, not for addresses scraped from websites (see `scraped_address`).


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:address |
| native | gc:address |




## LinkML Source

<details>
```yaml
name: address
description: Physical street address of the church or user.
comments:
- 'This is the official mailing or street address, suitable for postal delivery and
  mapping.

  Always include street number, street name, and any suite or apartment details if
  applicable.

  Follow the local postal format for the country (e.g., street before city in the
  US).

  Avoid using P.O. boxes unless it is the only available mailing address for the entity.

  For international addresses, include all relevant locality and region information.

  Use this slot for the canonical address, not for addresses scraped from websites
  (see `scraped_address`).

  '
examples:
- value: 123 Main St, Springfield, IL 62704
  description: Standard U.S. street address.
- value: 10 Downing St, London SW1A 2AA
  description: UK address with postal code.
in_subset:
- church_core
- public
from_schema: https://global.church/schema
rank: 1000
alias: address
domain_of:
- Church
range: string

```
</details>