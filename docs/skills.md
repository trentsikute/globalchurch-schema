

# Slot: skills 


_List of user skills._





URI: [gc:skills](https://global.church/schema/skills)
Alias: skills

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [User](User.md) | A registered platform user |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| ["photography", "youth_ministry", "python"] |

## Comments

* Use a controlled list where possible (e.g., “photography”, “youth_ministry”, “python”).
This slot is multivalued—store each skill as a separate list item.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:skills |
| native | gc:skills |
| exact | schema:skills |




## LinkML Source

<details>
```yaml
name: skills
description: List of user skills.
comments:
- 'Use a controlled list where possible (e.g., “photography”, “youth_ministry”, “python”).

  This slot is multivalued—store each skill as a separate list item.

  '
examples:
- value: '["photography", "youth_ministry", "python"]'
  description: Three discrete skills as a JSON array string.
in_subset:
- private
from_schema: https://global.church/schema
exact_mappings:
- schema:skills
rank: 1000
alias: skills
domain_of:
- User
range: string
multivalued: true

```
</details>