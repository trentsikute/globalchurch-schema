

# Slot: interests 


_User’s interests or ministry areas._





URI: [gc:interests](https://global.church/schema/interests)
Alias: interests

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
| missions, photography, discipleship |
| youth_ministry |

## Comments

* Free text or tags describing ministry passions (e.g., “missions”, “children”, “tech”).
Prefer consistent tagging conventions to improve searchability.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:interests |
| native | gc:interests |
| exact | schema:interest |




## LinkML Source

<details>
```yaml
name: interests
description: User’s interests or ministry areas.
comments:
- 'Free text or tags describing ministry passions (e.g., “missions”, “children”, “tech”).

  Prefer consistent tagging conventions to improve searchability.

  '
examples:
- value: missions, photography, discipleship
  description: Comma-separated input that will be normalized.
- value: youth_ministry
  description: Single interest term.
in_subset:
- private
from_schema: https://global.church/schema
exact_mappings:
- schema:interest
rank: 1000
alias: interests
domain_of:
- User
range: string

```
</details>