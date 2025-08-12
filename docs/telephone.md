

# Slot: telephone 


_User’s phone number (E.164)._





URI: [gc:telephone](https://global.church/schema/telephone)
Alias: telephone

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [User](User.md) | A registered platform user |  no  |







## Properties

* Range: [PhoneE164](PhoneE164.md)






## Examples

| Value |
| --- |
| +13105551234 |
| +442071838750 |

## Comments

* Store numbers in E.164 format (e.g., +14155552671). Country code is required.
Do not include spaces, parentheses, or dashes. For church phone, use `phone` slot.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:telephone |
| native | gc:telephone |
| exact | schema:telephone |




## LinkML Source

<details>
```yaml
name: telephone
description: User’s phone number (E.164).
comments:
- 'Store numbers in E.164 format (e.g., +14155552671). Country code is required.

  Do not include spaces, parentheses, or dashes. For church phone, use `phone` slot.

  '
examples:
- value: '+13105551234'
  description: US number in E.164 format.
- value: '+442071838750'
  description: UK number in E.164 format.
in_subset:
- internal
- pii
from_schema: https://global.church/schema
exact_mappings:
- schema:telephone
rank: 1000
alias: telephone
domain_of:
- User
range: phone_e164

```
</details>