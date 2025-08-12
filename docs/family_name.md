

# Slot: family_name 


_User’s last (family) name._





URI: [gc:family_name](https://global.church/schema/family_name)
Alias: family_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [User](User.md) | A registered platform user |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| Sikute |
| O'Neil |

## Comments

* Store the surname only. Do not include suffixes (e.g., Jr., III) or prefixes (e.g., Dr.).
If the person has a single name, leave this blank and use given_name only.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:family_name |
| native | gc:family_name |
| exact | schema:familyName |




## LinkML Source

<details>
```yaml
name: family_name
description: User’s last (family) name.
comments:
- 'Store the surname only. Do not include suffixes (e.g., Jr., III) or prefixes (e.g.,
  Dr.).

  If the person has a single name, leave this blank and use given_name only.

  '
examples:
- value: Sikute
  description: Standard family name.
- value: O'Neil
  description: Family name with punctuation.
in_subset:
- user_core
- private
- pii
from_schema: https://global.church/schema
exact_mappings:
- schema:familyName
rank: 1000
alias: family_name
domain_of:
- User
range: string

```
</details>