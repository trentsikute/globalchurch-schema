

# Slot: telephone 


_Phone number (international format recommended)._





URI: [gc:telephone](https://global.church/schema/telephone)
Alias: telephone

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [User](User.md) | A registered platform user |  no  |






## Properties

* Range: [PhoneE164](PhoneE164.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:telephone |
| native | gc:telephone |
| exact | schema:telephone |




## LinkML Source

<details>
```yaml
name: telephone
description: Phone number (international format recommended).
in_subset:
- internal
- pii
from_schema: https://global.church/schema
exact_mappings:
- schema:telephone
rank: 1000
alias: telephone
domain_of:
- User
range: phone_e164

```
</details>