

# Slot: phone 


_Official phone number for the church._





URI: [gc:phone](https://global.church/schema/phone)
Alias: phone

<!-- no inheritance hierarchy -->







## Properties

* Range: [PhoneE164](PhoneE164.md)





## Examples

| Value |
| --- |
| +13105551234 |
| +442071838750 |

## Comments

* Store the main contact number for the church in E.164 format (e.g., +14155552671).
Do not include user or staff personal numbers.
Numbers should be validated for correct format and country code.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:phone |
| native | gc:phone |
| exact | schema:telephone |




## LinkML Source

<details>
```yaml
name: phone
description: Official phone number for the church.
comments:
- 'Store the main contact number for the church in E.164 format (e.g., +14155552671).

  Do not include user or staff personal numbers.

  Numbers should be validated for correct format and country code.

  '
examples:
- value: '+13105551234'
  description: US church phone number.
- value: '+442071838750'
  description: UK church phone number.
in_subset:
- public
- overture
- enrichment
from_schema: https://global.church/schema
exact_mappings:
- schema:telephone
rank: 1000
alias: phone
range: phone_e164

```
</details>