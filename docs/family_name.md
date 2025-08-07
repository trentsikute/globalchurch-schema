

# Slot: family_name 


_Last name._





URI: [gc:family_name](https://global.church/schema/family_name)
Alias: family_name

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
| self | gc:family_name |
| native | gc:family_name |
| exact | schema:familyName |




## LinkML Source

<details>
```yaml
name: family_name
description: Last name.
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