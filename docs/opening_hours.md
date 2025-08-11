

# Slot: opening_hours 


_Church opening hours or service schedule._





URI: [gc:opening_hours](https://global.church/schema/opening_hours)
Alias: opening_hours

<!-- no inheritance hierarchy -->







## Properties

* Range: [String](String.md)





## Examples

| Value |
| --- |
| Sun 09:00-11:00, Wed 19:00-20:30 |
| Mo-Fr 09:00-17:00 |

## Comments

* Use either free text or a structured format to describe when the church is open or services are held.
For structured data, use the schema.org OpeningHours format (e.g., "Mo-Fr 09:00-17:00").
May include special service times or holiday exceptions.


## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:opening_hours |
| native | gc:opening_hours |
| exact | schema:openingHours, schema:openingHoursSpecification |




## LinkML Source

<details>
```yaml
name: opening_hours
description: Church opening hours or service schedule.
comments:
- 'Use either free text or a structured format to describe when the church is open
  or services are held.

  For structured data, use the schema.org OpeningHours format (e.g., "Mo-Fr 09:00-17:00").

  May include special service times or holiday exceptions.

  '
examples:
- value: Sun 09:00-11:00, Wed 19:00-20:30
  description: Typical service times.
- value: Mo-Fr 09:00-17:00
  description: Weekday opening hours.
in_subset:
- public
from_schema: https://global.church/schema
exact_mappings:
- schema:openingHours
- schema:openingHoursSpecification
rank: 1000
alias: opening_hours
range: string

```
</details>