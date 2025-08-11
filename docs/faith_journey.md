

# Slot: faith_journey 


_Narrative of the user’s faith journey._





URI: [gc:faith_journey](https://global.church/schema/faith_journey)
Alias: faith_journey

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
| Came to faith in 2016; baptized in 2017; serving in college ministry. |
| Exploring faith; interested in Alpha course. |

## Comments

* Long-form text. May include testimony, baptism date, or ministry milestones.
Avoid storing sensitive counseling notes in this field.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:faith_journey |
| native | gc:faith_journey |




## LinkML Source

<details>
```yaml
name: faith_journey
description: Narrative of the user’s faith journey.
comments:
- 'Long-form text. May include testimony, baptism date, or ministry milestones.

  Avoid storing sensitive counseling notes in this field.

  '
examples:
- value: Came to faith in 2016; baptized in 2017; serving in college ministry.
  description: Concise narrative.
- value: Exploring faith; interested in Alpha course.
  description: Short current-state note.
in_subset:
- internal
from_schema: https://global.church/schema
rank: 1000
alias: faith_journey
domain_of:
- User
range: string

```
</details>