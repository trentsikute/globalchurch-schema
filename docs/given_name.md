

# Slot: given_name 


_User’s first (given) name._





URI: [gc:given_name](https://global.church/schema/given_name)
Alias: given_name

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
| Ava |
| Jean-Luc |

## Comments

* Use the person’s preferred first name. Do not include middle names or initials here.
For organizations or teams, this slot should be left empty.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:given_name |
| native | gc:given_name |
| exact | schema:givenName |




## LinkML Source

<details>
```yaml
name: given_name
description: User’s first (given) name.
comments:
- 'Use the person’s preferred first name. Do not include middle names or initials
  here.

  For organizations or teams, this slot should be left empty.

  '
examples:
- value: Ava
  description: Simple given name.
- value: Jean-Luc
  description: Hyphenated given name.
in_subset:
- user_core
- private
- pii
from_schema: https://global.church/schema
exact_mappings:
- schema:givenName
rank: 1000
alias: given_name
domain_of:
- User
range: string

```
</details>