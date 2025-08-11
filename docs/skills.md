

# Slot: skills 


_Comma-separated list of user skills._





URI: [gc:skills](https://global.church/schema/skills)
Alias: skills

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [User](User.md) | A registered platform user |  no  |






## Properties

* Range: [String](String.md)




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
description: Comma-separated list of user skills.
in_subset:
- internal
from_schema: https://global.church/schema
exact_mappings:
- schema:skills
rank: 1000
alias: skills
domain_of:
- User
range: string

```
</details>