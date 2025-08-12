

# Slot: scraped_address 


_Postal address extracted from the website._





URI: [gc:scraped_address](https://global.church/schema/scraped_address)
Alias: scraped_address

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
| 456 Ocean Ave, Malibu, CA 90265 |

## Comments

* Use when the canonical `address` is not available or differs from the site.
This value may be noisy and should be normalized or validated before publishing.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:scraped_address |
| native | gc:scraped_address |
| exact | schema:address |




## LinkML Source

<details>
```yaml
name: scraped_address
description: Postal address extracted from the website.
comments:
- 'Use when the canonical `address` is not available or differs from the site.

  This value may be noisy and should be normalized or validated before publishing.

  '
examples:
- value: 456 Ocean Ave, Malibu, CA 90265
  description: Address parsed from the footer.
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
exact_mappings:
- schema:address
rank: 1000
alias: scraped_address
domain_of:
- Church
range: string

```
</details>