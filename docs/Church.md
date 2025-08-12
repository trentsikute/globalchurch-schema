

# Class: Church 


_A distinct church congregation._





URI: [gc:Church](https://global.church/schema/Church)











<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [church_id](church_id.md) | 1 <br/> [Uuid](Uuid.md) | Global | direct |
| [gers_id](gers_id.md) | 1 <br/> [String](String.md) | Government/Ecclesiastical Registry System identifier | direct |
| [name](name.md) | 1 <br/> [String](String.md) | Official church name | direct |
| [pipeline_status](pipeline_status.md) | 1 <br/> [String](String.md) | Current enrichment pipeline stage | direct |
| [latitude](latitude.md) | 1 <br/> [Float](Float.md) | Latitude in decimal degrees | direct |
| [longitude](longitude.md) | 1 <br/> [Float](Float.md) | Longitude in decimal degrees | direct |
| [address](address.md) | 1 <br/> [String](String.md) | Physical street address of the church or user | direct |
| [locality](locality.md) | 1 <br/> [String](String.md) | City or locality where the church is located | direct |
| [region](region.md) | 1 <br/> [String](String.md) | State, province, or administrative region | direct |
| [postal_code](postal_code.md) | 1 <br/> [String](String.md) | Postal code or ZIP code for the address | direct |
| [country](country.md) | 1 <br/> [IsoCountryCode](IsoCountryCode.md) | Country code in ISO 3166-1 alpha-2 format | direct |
| [website](website.md) | 0..1 <br/> [Uri](Uri.md) | Full website URL for the church | direct |
| [website_root](website_root.md) | 0..1 <br/> [Uri](Uri.md) | Root URL of the church website (scheme and domain only) | direct |
| [search_blob](search_blob.md) | 0..1 <br/> [String](String.md) | Concatenated text of searchable fields for indexing | direct |
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
| self | gc:Church |
| native | gc:Church |
| undefined | schema:Church, schema:Organization |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Church
description: A distinct church congregation.
in_subset:
- public
from_schema: https://global.church/schema
mappings:
- schema:Church
- schema:Organization
rank: 1000
slots:
- church_id
- gers_id
- name
- pipeline_status
- latitude
- longitude
- address
- locality
- region
- postal_code
- country
- website
- website_root
- search_blob
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
slot_usage:
  church_id:
    name: church_id
    required: true
  name:
    name: name
    required: true
  pipeline_status:
    name: pipeline_status
    required: true
  latitude:
    name: latitude
    required: true
  longitude:
    name: longitude
    required: true
  address:
    name: address
    required: true
  locality:
    name: locality
    required: true
  region:
    name: region
    required: true
  postal_code:
    name: postal_code
    required: true
  country:
    name: country
    required: true

```
</details>

### Induced

<details>
```yaml
name: Church
description: A distinct church congregation.
in_subset:
- public
from_schema: https://global.church/schema
mappings:
- schema:Church
- schema:Organization
rank: 1000
slot_usage:
  church_id:
    name: church_id
    required: true
  name:
    name: name
    required: true
  pipeline_status:
    name: pipeline_status
    required: true
  latitude:
    name: latitude
    required: true
  longitude:
    name: longitude
    required: true
  address:
    name: address
    required: true
  locality:
    name: locality
    required: true
  region:
    name: region
    required: true
  postal_code:
    name: postal_code
    required: true
  country:
    name: country
    required: true
attributes:
  church_id:
    name: church_id
    description: Global.Church-issued ID for a church.
    comments:
    - 'Primary key for the Church entity. Stable and non-reassignable.

      Used as the foreign key for ChurchWebsiteText, EnrichedData, and other related
      records.

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
    owner: Church
    domain_of:
    - Church
    - ChurchWebsiteText
    range: uuid
    required: true
  gers_id:
    name: gers_id
    description: Government/Ecclesiastical Registry System identifier.
    comments:
    - 'External registry identifier used for cross-referencing with official listings.

      May not exist for all churches.

      '
    examples:
    - value: GERS-CA-00012345
      description: Sample registry ID.
    in_subset:
    - overture
    - public
    from_schema: https://global.church/schema
    rank: 1000
    identifier: true
    alias: gers_id
    owner: Church
    domain_of:
    - Church
    - Overture
    range: string
    required: true
  name:
    name: name
    description: Official church name.
    comments:
    - 'Use the legal or commonly recognized name (e.g., “Grace Community Church”).

      If there is a campus name or colloquial short name, store it in `alternate_name`.

      '
    examples:
    - value: Grace Community Church
      description: Formal church name.
    - value: Grace Church Malibu
      description: Name with locality qualifier.
    in_subset:
    - church_core
    - public
    from_schema: https://global.church/schema
    exact_mappings:
    - schema:name
    rank: 1000
    alias: name
    owner: Church
    domain_of:
    - Church
    range: string
    required: true
  pipeline_status:
    name: pipeline_status
    description: Current enrichment pipeline stage.
    comments:
    - 'Suggested stages: RAW → CLEAN → ENRICHED → VALIDATED.

      RAW: ingested with minimal checks.

      CLEAN: deduplicated & normalized.

      ENRICHED: scraped/AI fields added.

      VALIDATED: human-reviewed.

      '
    examples:
    - value: approved_for_gc_db
      description: Approved for Global.Church database.
    - value: no_website
      description: Entity lacks a website.
    in_subset:
    - internal
    from_schema: https://global.church/schema
    rank: 1000
    alias: pipeline_status
    owner: Church
    domain_of:
    - Church
    range: string
    required: true
  latitude:
    name: latitude
    description: Latitude in decimal degrees.
    comments:
    - 'Use WGS84 decimal degrees. South is negative.

      Precision of 5–6 decimal places is typically sufficient (~1–10 meters).

      '
    examples:
    - value: '34.0259'
      description: Approximate latitude for Malibu, CA.
    - value: '-33.8688'
      description: Southern hemisphere example (Sydney).
    in_subset:
    - church_core
    - public
    from_schema: https://global.church/schema
    exact_mappings:
    - schema:latitude
    rank: 1000
    alias: latitude
    owner: Church
    domain_of:
    - Church
    range: float
    required: true
    minimum_value: -90
    maximum_value: 90
  longitude:
    name: longitude
    description: Longitude in decimal degrees.
    comments:
    - 'Use WGS84 decimal degrees. West is negative.

      Keep latitude/longitude pairs from the same source to avoid mismatch.

      '
    examples:
    - value: '-118.7798'
      description: Approximate longitude for Malibu, CA.
    - value: '151.2093'
      description: Eastern hemisphere example (Sydney).
    in_subset:
    - church_core
    - public
    from_schema: https://global.church/schema
    exact_mappings:
    - schema:longitude
    rank: 1000
    alias: longitude
    owner: Church
    domain_of:
    - Church
    range: float
    required: true
    minimum_value: -180
    maximum_value: 180
  address:
    name: address
    description: Physical street address of the church or user.
    comments:
    - 'This is the official mailing or street address, suitable for postal delivery
      and mapping.

      Always include street number, street name, and any suite or apartment details
      if applicable.

      Follow the local postal format for the country (e.g., street before city in
      the US).

      Avoid using P.O. boxes unless it is the only available mailing address for the
      entity.

      For international addresses, include all relevant locality and region information.

      Use this slot for the canonical address, not for addresses scraped from websites
      (see `scraped_address`).

      '
    examples:
    - value: 123 Main St, Springfield, IL 62704
      description: Standard U.S. street address.
    - value: 10 Downing St, London SW1A 2AA
      description: UK address with postal code.
    in_subset:
    - church_core
    - public
    from_schema: https://global.church/schema
    rank: 1000
    alias: address
    owner: Church
    domain_of:
    - Church
    range: string
    required: true
  locality:
    name: locality
    description: City or locality where the church is located.
    comments:
    - 'The city, town, or locality where the church''s primary address is situated.

      Use the official or most commonly recognized municipality name.

      This value should match the locality as used by local postal authorities.

      For rural areas without a city, use the nearest recognized locality.

      '
    examples:
    - value: Springfield
      description: US city.
    - value: Sydney
      description: Major city in Australia.
    in_subset:
    - church_core
    - public
    from_schema: https://global.church/schema
    exact_mappings:
    - schema:addressLocality
    rank: 1000
    alias: locality
    owner: Church
    domain_of:
    - Church
    range: string
    required: true
  region:
    name: region
    description: State, province, or administrative region.
    comments:
    - 'The primary administrative subdivision for the locality, such as state (US),
      province (Canada), or region (EU).

      Use the full name or standard abbreviation as appropriate for the country.

      For countries without such subdivisions, leave this slot empty.

      '
    examples:
    - value: CA
      description: California (US state abbreviation).
    - value: New South Wales
      description: Australian state.
    in_subset:
    - church_core
    - public
    from_schema: https://global.church/schema
    exact_mappings:
    - schema:addressRegion
    rank: 1000
    alias: region
    owner: Church
    domain_of:
    - Church
    range: string
    required: true
  postal_code:
    name: postal_code
    description: Postal code or ZIP code for the address.
    comments:
    - 'The postal (ZIP) code as assigned by the national postal authority.

      Use the correct format for the country (e.g., 12345 or 12345-6789 in the US,
      SW1A 2AA in the UK).

      Always include this value for postal addresses if available.

      '
    examples:
    - value: '62704'
      description: US ZIP code.
    - value: SW1A 2AA
      description: UK postal code.
    in_subset:
    - church_core
    - public
    from_schema: https://global.church/schema
    exact_mappings:
    - schema:postalCode
    rank: 1000
    alias: postal_code
    owner: Church
    domain_of:
    - Church
    range: string
    required: true
  country:
    name: country
    description: Country code in ISO 3166-1 alpha-2 format.
    comments:
    - 'Use the two-letter ISO 3166-1 alpha-2 code (e.g., US, GB, AU).

      This field is required for all church records.

      Do not use full country names or three-letter codes.

      '
    examples:
    - value: US
      description: United States.
    - value: NG
      description: Nigeria.
    in_subset:
    - church_core
    - public
    from_schema: https://global.church/schema
    exact_mappings:
    - schema:addressCountry
    rank: 1000
    alias: country
    owner: Church
    domain_of:
    - Church
    range: iso_country_code
    required: true
  website:
    name: website
    description: Full website URL for the church.
    comments:
    - 'Provide the complete URL, including scheme (http/https).

      Use the main public-facing website for the church.

      Exclude social media links (see `instagram_url`, `youtube_url`).

      '
    examples:
    - value: https://gracechurch.org
      description: Church homepage.
    - value: https://stpauls-sydney.org.au
      description: Australian church website.
    in_subset:
    - public
    from_schema: https://global.church/schema
    exact_mappings:
    - schema:url
    rank: 1000
    alias: website
    owner: Church
    domain_of:
    - Church
    range: uri
  website_root:
    name: website_root
    description: Root URL of the church website (scheme and domain only).
    comments:
    - 'The canonical root domain for the church website, e.g., https://example.org.

      Used for web scraping and deduplication.

      Exclude any path, query, or fragment components.

      '
    examples:
    - value: https://gracechurch.org
      description: Root domain for scraping.
    - value: https://stpauls-sydney.org.au
      description: Australian church root domain.
    in_subset:
    - internal
    from_schema: https://global.church/schema
    rank: 1000
    alias: website_root
    owner: Church
    domain_of:
    - Church
    range: uri
  search_blob:
    name: search_blob
    description: Concatenated text of searchable fields for indexing.
    comments:
    - 'This slot is used internally to store a combined string of key fields

      (e.g., name, address, keywords) for full-text search indexing.

      Not intended for direct display or export.

      '
    examples:
    - value: Grace Community Church 123 Main St Springfield CA 62704 US
      description: Combined fields for search.
    in_subset:
    - internal
    from_schema: https://global.church/schema
    rank: 1000
    alias: search_blob
    owner: Church
    domain_of:
    - Church
    range: string
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
    owner: Church
    domain_of:
    - Church
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
    owner: Church
    domain_of:
    - Church
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
    owner: Church
    domain_of:
    - Church
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
    owner: Church
    domain_of:
    - Church
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
    owner: Church
    domain_of:
    - Church
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
    owner: Church
    domain_of:
    - Church
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
    owner: Church
    domain_of:
    - Church
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
    owner: Church
    domain_of:
    - Church
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
    owner: Church
    domain_of:
    - Church
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
    owner: Church
    domain_of:
    - Church
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
    owner: Church
    domain_of:
    - Church
    range: string

```
</details>