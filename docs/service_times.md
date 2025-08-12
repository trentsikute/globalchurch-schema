

# Slot: service_times 


_Service times for public gatherings._





URI: [gc:service_times](https://global.church/schema/service_times)
Alias: service_times

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
| Sundays 9:00 & 11:00; Wednesdays 7:00 |
| Sat 18:00 (Español), Sun 10:00 (English) |

## Comments

* Free text or structured patterns (e.g., “Sun 9:00 & 11:00; Wed 19:00”).
If multiple campuses or languages differ, note this in `service_languages` and
`programs_offered` where appropriate.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:service_times |
| native | gc:service_times |




## LinkML Source

<details>
```yaml
name: service_times
description: Service times for public gatherings.
comments:
- 'Free text or structured patterns (e.g., “Sun 9:00 & 11:00; Wed 19:00”).

  If multiple campuses or languages differ, note this in `service_languages` and

  `programs_offered` where appropriate.

  '
examples:
- value: Sundays 9:00 & 11:00; Wednesdays 7:00
  description: Weekly cadence.
- value: Sat 18:00 (Español), Sun 10:00 (English)
  description: Bilingual schedule.
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
rank: 1000
alias: service_times
domain_of:
- Church
range: string

```
</details>