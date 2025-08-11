

# Slot: country 


_Country code in ISO 3166-1 alpha-2 format._





URI: [gc:country](https://global.church/schema/country)
Alias: country

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  yes  |






## Properties

* Range: [IsoCountryCode](IsoCountryCode.md)





## Examples

| Value |
| --- |
| US |
| NG |

## Comments

* Use the two-letter ISO 3166-1 alpha-2 code (e.g., US, GB, AU).
This field is required for all church records.
Do not use full country names or three-letter codes.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:country |
| native | gc:country |
| exact | schema:addressCountry |




## LinkML Source

<details>
```yaml
name: country
description: Country code in ISO 3166-1 alpha-2 format.
comments:
- 'Use the two-letter ISO 3166-1 alpha-2 code (e.g., US, GB, AU).

  This field is required for all church records.

  Do not use full country names or three-letter codes.

  '
examples:
- value: US
  description: United States.
- value: NG
  description: Nigeria.
in_subset:
- church_core
- public
from_schema: https://global.church/schema
exact_mappings:
- schema:addressCountry
rank: 1000
alias: country
domain_of:
- Church
range: iso_country_code

```
</details>