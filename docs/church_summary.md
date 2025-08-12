

# Slot: church_summary 


_Concise public summary of the church._





URI: [gc:church_summary](https://global.church/schema/church_summary)
Alias: church_summary

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
| Multi-generational church serving Malibu with Sunday services at 9 & 11am and active youth and outreach programs. |

## Comments

* 1–3 sentences describing the congregation, location, service style, and distinctives.
Intended for profile cards or search results. Keep under ~300 characters.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:church_summary |
| native | gc:church_summary |




## LinkML Source

<details>
```yaml
name: church_summary
description: Concise public summary of the church.
comments:
- '1–3 sentences describing the congregation, location, service style, and distinctives.

  Intended for profile cards or search results. Keep under ~300 characters.

  '
examples:
- value: Multi-generational church serving Malibu with Sunday services at 9 & 11am
    and active youth and outreach programs.
  description: Short profile blurb.
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
rank: 1000
alias: church_summary
domain_of:
- Church
range: string

```
</details>