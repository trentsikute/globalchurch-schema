

# Class: EnrichedData 


_AI-enriched attributes extracted from the church website and socials._





URI: [gc:EnrichedData](https://global.church/schema/EnrichedData)










<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [church_id](church_id.md) | 1 <br/> [Uuid](Uuid.md) | Global | direct |
| [service_times](service_times.md) | 0..1 <br/> [String](String.md) | Service times for public gatherings | direct |
| [church_beliefs_url](church_beliefs_url.md) | 0..1 <br/> [Uri](Uri.md) | URL for the church’s statement of beliefs/faith | direct |
| [trinitarian_beliefs](trinitarian_beliefs.md) | 0..1 <br/> [Boolean](Boolean.md) | Whether the church affirms classical Trinitarian doctrine | direct |
| [belief_type](belief_type.md) | 0..1 <br/> [BeliefTypeEnum](BeliefTypeEnum.md) | Denomination / church type category | direct |
| [scraped_email](scraped_email.md) | 0..1 <br/> [email](email.md) | Public email address extracted from the website | direct |
| [instagram_url](instagram_url.md) | 0..1 <br/> [Uri](Uri.md) | Instagram profile URL | direct |
| [youtube_url](youtube_url.md) | 0..1 <br/> [Uri](Uri.md) | YouTube channel URL | direct |
| [service_languages](service_languages.md) | * <br/> [String](String.md) | Languages in which services are offered | direct |
| [scraped_address](scraped_address.md) | 0..1 <br/> [String](String.md) | Postal address extracted from the website | direct |
| [programs_offered](programs_offered.md) | * <br/> [String](String.md) | Programs or ministries the church offers | direct |
| [church_summary](church_summary.md) | 0..1 <br/> [String](String.md) | Concise public summary of the church | direct |










## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:EnrichedData |
| native | gc:EnrichedData |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EnrichedData
description: AI-enriched attributes extracted from the church website and socials.
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
rank: 1000
slots:
- church_id
- service_times
- church_beliefs_url
- trinitarian_beliefs
- belief_type
- scraped_email
- instagram_url
- youtube_url
- service_languages
- scraped_address
- programs_offered
- church_summary

```
</details>

### Induced

<details>
```yaml
name: EnrichedData
description: AI-enriched attributes extracted from the church website and socials.
in_subset:
- public
- enrichment
from_schema: https://global.church/schema
rank: 1000
attributes:
  church_id:
    name: church_id
    description: Global.Church-issued ID for a church.
    comments:
    - 'Primary key for the Church entity. Stable and non-reassignable.

      Used as the foreign key for ChurchWebsite, EnrichedData, and other related records.

      '
    examples:
    - value: 9e1c2a7d-4c33-4b8b-9d7a-1a2b3c4d5e6f
      description: Example church UUID.
    in_subset:
    - church_core
    - public
    from_schema: https://global.church/schema
    rank: 1000
    identifier: true
    alias: church_id
    owner: EnrichedData
    domain_of:
    - Church
    - ChurchWebsite
    - EnrichedData
    range: uuid
    required: true
  service_times:
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
    owner: EnrichedData
    domain_of:
    - EnrichedData
    range: string
  church_beliefs_url:
    name: church_beliefs_url
    description: URL for the church’s statement of beliefs/faith.
    comments:
    - 'Prefer the canonical “Beliefs” page for doctrinal summaries.

      If multiple pages exist, choose the most comprehensive source.

      '
    examples:
    - value: https://gracechurch.org/beliefs
      description: Canonical beliefs page.
    in_subset:
    - public
    - enrichment
    from_schema: https://global.church/schema
    rank: 1000
    alias: church_beliefs_url
    owner: EnrichedData
    domain_of:
    - EnrichedData
    range: uri
  trinitarian_beliefs:
    name: trinitarian_beliefs
    description: Whether the church affirms classical Trinitarian doctrine.
    comments:
    - 'Boolean derived from site language (e.g., statements referencing Father, Son,
      Holy Spirit).

      When unknown or ambiguous, leave unset rather than guessing.

      '
    examples:
    - value: 'true'
      description: Affirmed on the Beliefs page.
    - value: 'false'
      description: Explicitly non-Trinitarian statement.
    in_subset:
    - public
    - enrichment
    from_schema: https://global.church/schema
    rank: 1000
    alias: trinitarian_beliefs
    owner: EnrichedData
    domain_of:
    - EnrichedData
    range: boolean
  belief_type:
    name: belief_type
    description: 'Denomination / church type category.

      Classifies the church into a top-level Christian family as defined by BeliefTypeEnum.

      Based on the Harvest Information Standards (HIS) Registry of Religions.

      '
    comments:
    - 'Use the controlled values in BeliefTypeEnum. When unclear, set `unknown`.

      You may revise this after human review.

      '
    examples:
    - value: protestant
      description: Derived from the site’s denomination statement.
    - value: unknown
      description: Insufficient info to classify.
    in_subset:
    - public
    - enrichment
    from_schema: https://global.church/schema
    rank: 1000
    alias: belief_type
    owner: EnrichedData
    domain_of:
    - EnrichedData
    range: BeliefTypeEnum
  scraped_email:
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
    owner: EnrichedData
    domain_of:
    - EnrichedData
    range: email
  instagram_url:
    name: instagram_url
    description: Instagram profile URL.
    comments:
    - 'Prefer the canonical profile (not a hashtag or location page).

      Normalize to the https scheme.

      '
    examples:
    - value: https://www.instagram.com/gracechurch/
      description: Canonical Instagram URL.
    in_subset:
    - public
    - enrichment
    from_schema: https://global.church/schema
    exact_mappings:
    - schema:sameAs
    rank: 1000
    alias: instagram_url
    owner: EnrichedData
    domain_of:
    - EnrichedData
    range: uri
  youtube_url:
    name: youtube_url
    description: YouTube channel URL.
    comments:
    - 'Prefer the canonical channel or handle URL (not individual video URLs).

      Normalize to https and include trailing slash when appropriate.

      '
    examples:
    - value: https://www.youtube.com/@GraceChurch
      description: Channel handle URL.
    in_subset:
    - public
    - enrichment
    from_schema: https://global.church/schema
    exact_mappings:
    - schema:sameAs
    rank: 1000
    alias: youtube_url
    owner: EnrichedData
    domain_of:
    - EnrichedData
    range: uri
  service_languages:
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
    owner: EnrichedData
    domain_of:
    - EnrichedData
    range: string
    multivalued: true
  scraped_address:
    name: scraped_address
    description: Postal address extracted from the website.
    comments:
    - 'Use when the canonical `address` is not available or differs from the site.

      This value may be noisy and should be normalized or validated before publishing.

      '
    examples:
    - value: 456 Ocean Ave, Malibu, CA 90265
      description: Address parsed from the footer.
    in_subset:
    - public
    - enrichment
    from_schema: https://global.church/schema
    exact_mappings:
    - schema:address
    rank: 1000
    alias: scraped_address
    owner: EnrichedData
    domain_of:
    - EnrichedData
    range: string
  programs_offered:
    name: programs_offered
    description: Programs or ministries the church offers.
    comments:
    - 'List distinct program names (e.g., “Youth”, “Alpha”, “Food Pantry”).

      Prefer stable, human-readable labels; avoid internal codes in public data.

      '
    examples:
    - value: '["Youth Ministry", "Food Pantry", "Alpha Course"]'
      description: Three public-facing programs as a JSON array string.
    in_subset:
    - public
    - enrichment
    from_schema: https://global.church/schema
    exact_mappings:
    - schema:service
    rank: 1000
    alias: programs_offered
    owner: EnrichedData
    domain_of:
    - EnrichedData
    range: string
    multivalued: true
  church_summary:
    name: church_summary
    description: Concise public summary of the church.
    comments:
    - '1–3 sentences describing the congregation, location, service style, and distinctives.

      Intended for profile cards or search results. Keep under ~300 characters.

      '
    examples:
    - value: Multi-generational church serving Malibu with Sunday services at 9 &
        11am and active youth and outreach programs.
      description: Short profile blurb.
    in_subset:
    - public
    - enrichment
    from_schema: https://global.church/schema
    rank: 1000
    alias: church_summary
    owner: EnrichedData
    domain_of:
    - EnrichedData
    range: string

```
</details>