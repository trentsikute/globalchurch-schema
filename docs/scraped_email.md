

# Slot: scraped_email 


_Public email address extracted from the website._





URI: [gc:scraped_email](https://global.church/schema/scraped_email)
Alias: scraped_email

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  no  |







## Properties

* Range: [email](email.md)






## Examples

| Value |
| --- |
| info@gracechurch.org |
| office@stpauls-sydney.org.au |

## Comments

* Only store addresses published for church contact (office@, info@).
Do not store personal staff emails unless explicitly public and necessary.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:scraped_email |
| native | gc:scraped_email |
| exact | schema:email |




## LinkML Source

<details>
```yaml
name: scraped_email
description: Public email address extracted from the website.
comments:
- 'Only store addresses published for church contact (office@, info@).

  Do not store personal staff emails unless explicitly public and necessary.

  '
examples:
- value: info@gracechurch.org
  description: Generic church inbox.
- value: office@stpauls-sydney.org.au
  description: Office contact.
in_subset:
- internal
- pii
- enrichment
from_schema: https://global.church/schema
exact_mappings:
- schema:email
rank: 1000
alias: scraped_email
domain_of:
- Church
range: email

```
</details>