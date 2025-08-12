

# Slot: social_media 


_List of social media handles or URLs associated with the church._





URI: [gc:social_media](https://global.church/schema/social_media)
Alias: social_media

<!-- no inheritance hierarchy -->








## Properties

* Range: [String](String.md)

* Multivalued: True






## Examples

| Value |
| --- |
| ["https://facebook.com/gracechurch", "@gracechurchmalibu"] |

## Comments

* May be a JSON object or a list of URLs/usernames for platforms such as Facebook, Twitter, Instagram, etc.
Provided by Overture Maps or extracted from the church website.
Use platform-specific slots (e.g., `instagram_url`) when available.


## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:social_media |
| native | gc:social_media |




## LinkML Source

<details>
```yaml
name: social_media
description: List of social media handles or URLs associated with the church.
comments:
- 'May be a JSON object or a list of URLs/usernames for platforms such as Facebook,
  Twitter, Instagram, etc.

  Provided by Overture Maps or extracted from the church website.

  Use platform-specific slots (e.g., `instagram_url`) when available.

  '
examples:
- value: '["https://facebook.com/gracechurch", "@gracechurchmalibu"]'
  description: Facebook URL and Twitter handle as a JSON array string.
in_subset:
- public
- overture
- enrichment
from_schema: https://global.church/schema
rank: 1000
alias: social_media
range: string
multivalued: true

```
</details>