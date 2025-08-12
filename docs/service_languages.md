

# Slot: service_languages 


_Languages in which services are offered._





URI: [gc:service_languages](https://global.church/schema/service_languages)
Alias: service_languages

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Church](Church.md) | A distinct church congregation |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| ["English", "Spanish"] |

## Comments

* Use ISO 639 language names or tags where possible (e.g., “en”, “es” or “English”, “Spanish”).
Include multiple entries for multilingual services/campuses.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:service_languages |
| native | gc:service_languages |
| exact | schema:inLanguage |




## LinkML Source

<details>
```yaml
name: service_languages
description: Languages in which services are offered.
comments:
- 'Use ISO 639 language names or tags where possible (e.g., “en”, “es” or “English”,
  “Spanish”).

  Include multiple entries for multilingual services/campuses.

  '
examples:
- value: '["English", "Spanish"]'
  description: Bilingual services as a JSON array string.
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
exact_mappings:
- schema:inLanguage
rank: 1000
alias: service_languages
domain_of:
- Church
range: string
multivalued: true

```
</details>