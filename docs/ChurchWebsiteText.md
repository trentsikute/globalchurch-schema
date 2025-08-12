

# Class: ChurchWebsiteText 


_Raw scrape artifacts captured from the church root URL. Not intended for general public use._





URI: [gc:ChurchWebsiteText](https://global.church/schema/ChurchWebsiteText)











<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [church_id](church_id.md) | 1 <br/> [Uuid](Uuid.md) | Global | direct |
| [root_scrape_text](root_scrape_text.md) | 0..1 <br/> [String](String.md) | Visible text content scraped from the website root page | direct |
| [root_scrape_buttons](root_scrape_buttons.md) | 0..1 <br/> [String](String.md) | Button texts captured on the root page | direct |
| [root_scrape_check](root_scrape_check.md) | 0..1 <br/> [String](String.md) | Checksum or status flag indicating scrape state | direct |
| [root_candidates](root_candidates.md) | * <br/> [String](String.md) | Candidate URLs extracted from the root page | direct |
| [candidates_text_and_links](candidates_text_and_links.md) | * <br/> [String](String.md) | Text snippets and associated links for candidate pages | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:ChurchWebsiteText |
| native | gc:ChurchWebsiteText |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ChurchWebsiteText
description: Raw scrape artifacts captured from the church root URL. Not intended
  for general public use.
in_subset:
- internal
- private
from_schema: https://global.church/schema
rank: 1000
slots:
- church_id
- root_scrape_text
- root_scrape_buttons
- root_scrape_check
- root_candidates
- candidates_text_and_links

```
</details>

### Induced

<details>
```yaml
name: ChurchWebsiteText
description: Raw scrape artifacts captured from the church root URL. Not intended
  for general public use.
in_subset:
- internal
- private
from_schema: https://global.church/schema
rank: 1000
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
    owner: ChurchWebsiteText
    domain_of:
    - Church
    - ChurchWebsiteText
    range: uuid
    required: true
  root_scrape_text:
    name: root_scrape_text
    description: Visible text content scraped from the website root page.
    comments:
    - 'The full visible text extracted from the HTML body of the root URL of the church
      website.

      Used for downstream enrichment, NLP, and data extraction.

      Not intended for public display; may contain headers, footers, and navigation
      text.

      For structured content, see other enrichment slots.

      '
    examples:
    - value: Welcome to Grace Community Church! Join us Sundays at 9am and 11am. Our
        mission is to serve Malibu and beyond...
      description: Scraped homepage text sample.
    in_subset:
    - internal
    from_schema: https://global.church/schema
    rank: 1000
    alias: root_scrape_text
    owner: ChurchWebsiteText
    domain_of:
    - ChurchWebsiteText
    range: string
  root_scrape_buttons:
    name: root_scrape_buttons
    description: Button texts captured on the root page.
    comments:
    - 'Capture the visible labels of clickable buttons/links from the root URL

      (e.g., “Plan a Visit”, “Give”, “Watch Live”). Useful for enrichment heuristics.

      This is raw scrape output and may include navigation or repeated items.

      '
    examples:
    - value: '["Plan a Visit", "Watch Live", "Give"]'
      description: Common calls-to-action from a church homepage as a JSON array string.
    in_subset:
    - internal
    from_schema: https://global.church/schema
    rank: 1000
    alias: root_scrape_buttons
    owner: ChurchWebsiteText
    domain_of:
    - ChurchWebsiteText
    range: string
  root_scrape_check:
    name: root_scrape_check
    description: Checksum or status flag indicating scrape state.
    comments:
    - 'Use for lightweight integrity checks (e.g., a hash of the DOM or a status string

      like “ok”, “blocked”, “timeout”). Helps detect page changes between scrapes.

      '
    examples:
    - value: sha256:3b2d9f3a…
      description: Digest of the normalized page content.
    - value: timeout
      description: Network timeout recorded during scraping.
    in_subset:
    - internal
    from_schema: https://global.church/schema
    rank: 1000
    alias: root_scrape_check
    owner: ChurchWebsiteText
    domain_of:
    - ChurchWebsiteText
    range: string
  root_candidates:
    name: root_candidates
    description: Candidate URLs extracted from the root page.
    comments:
    - 'Potential internal links to pages like “Beliefs”, “Ministries”, “Visit”, etc.

      Feed these into downstream enrichment for targeted scraping.

      Store fully qualified URLs when possible.

      '
    examples:
    - value: '["https://gracechurch.org/beliefs", "https://gracechurch.org/ministries"]'
      description: Two high-value candidate pages as a JSON array string.
    in_subset:
    - internal
    from_schema: https://global.church/schema
    rank: 1000
    alias: root_candidates
    owner: ChurchWebsiteText
    domain_of:
    - ChurchWebsiteText
    range: string
    multivalued: true
  candidates_text_and_links:
    name: candidates_text_and_links
    description: Text snippets and associated links for candidate pages.
    comments:
    - 'Use a consistent representation (e.g., JSON strings) pairing anchor text with
      href.

      Example object shape: {"text": "Beliefs", "url": "https://…/beliefs"}.

      Helps prioritize which candidate links are most relevant.

      '
    examples:
    - value: '["{\"text\": \"Beliefs\", \"url\": \"https://gracechurch.org/beliefs\"}",
        "{\"text\": \"Plan a Visit\", \"url\": \"https://gracechurch.org/visit\"}"]'
      description: Two text–link pairs serialized as a JSON array of JSON objects.
    in_subset:
    - internal
    from_schema: https://global.church/schema
    rank: 1000
    alias: candidates_text_and_links
    owner: ChurchWebsiteText
    domain_of:
    - ChurchWebsiteText
    range: string
    multivalued: true

```
</details>