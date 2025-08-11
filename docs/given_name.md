

# Slot: given_name 


_First name._





URI: [gc:given_name](https://global.church/schema/given_name)
Alias: given_name

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
| self | gc:given_name |
| native | gc:given_name |
| exact | schema:givenName |




## LinkML Source

<details>
```yaml
name: given_name
description: First name.
in_subset:
- user_core
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