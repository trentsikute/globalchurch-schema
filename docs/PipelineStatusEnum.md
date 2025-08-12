# Enum: PipelineStatusEnum 




_Stages in the enrichment pipeline for church data._



URI: [PipelineStatusEnum](PipelineStatusEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| approved_for_gc_db | None | Data has been reviewed and approved for inclusion in the Global |
| no_website | None | Church has no website or web presence |
| playwright_fail | None | Failed to scrape the church website using Playwright |
| explicitly_non_church | None | Entity is explicitly not a church (e |
| dns_fail | None | Failed to resolve the church's domain name |
| ai_scrape_failed | None | Failed to scrape the church website using AI methods |
| non_trinitarian_filter | None | Entity uses common non-Trinitarian terminology |
| ai_church_network | None | AI determined the entity's associated website belongs to a church network |
| explicitly_non_trinitarian | None | Entity is explicitly non-Trinitarian (e |
| parachurch_filter | None | Entity is a parachurch organization, not a church |
| ai_manual_review | None | Data requires manual review after AI processing |
| ai_non_trinitarian | None | AI determined the entity is non-Trinitarian |
| non_christian_terms | None | Entity uses terms not typically associated with Christian churches |
| gers_id_already_in_db | None | The GERS ID already exists in the Global |









## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema






## LinkML Source

<details>
```yaml
name: PipelineStatusEnum
description: Stages in the enrichment pipeline for church data.
from_schema: https://global.church/schema
rank: 1000
permissible_values:
  approved_for_gc_db:
    text: approved_for_gc_db
    description: Data has been reviewed and approved for inclusion in the Global.Church
      database.
    aliases:
    - Approved
  no_website:
    text: no_website
    description: Church has no website or web presence.
    aliases:
    - No Website
  playwright_fail:
    text: playwright_fail
    description: Failed to scrape the church website using Playwright.
    aliases:
    - Playwright Fail
  explicitly_non_church:
    text: explicitly_non_church
    description: Entity is explicitly not a church (e.g., secular organization).
    aliases:
    - Explicitly Non-Church
  dns_fail:
    text: dns_fail
    description: Failed to resolve the church's domain name.
    aliases:
    - DNS Fail
  ai_scrape_failed:
    text: ai_scrape_failed
    description: Failed to scrape the church website using AI methods.
    aliases:
    - AI Scrape Failed
  non_trinitarian_filter:
    text: non_trinitarian_filter
    description: Entity uses common non-Trinitarian terminology.
    aliases:
    - Non-Trinitarian Filter
  ai_church_network:
    text: ai_church_network
    description: AI determined the entity's associated website belongs to a church
      network.
    aliases:
    - AI Church Network
  explicitly_non_trinitarian:
    text: explicitly_non_trinitarian
    description: Entity is explicitly non-Trinitarian (e.g., Unitarian, Jehovah's
      Witness).
    aliases:
    - Explicitly Non-Trinitarian
  parachurch_filter:
    text: parachurch_filter
    description: Entity is a parachurch organization, not a church.
    aliases:
    - Parachurch Filter
  ai_manual_review:
    text: ai_manual_review
    description: Data requires manual review after AI processing.
    aliases:
    - AI Manual Review
  ai_non_trinitarian:
    text: ai_non_trinitarian
    description: AI determined the entity is non-Trinitarian.
    aliases:
    - AI Non-Trinitarian
  non_christian_terms:
    text: non_christian_terms
    description: Entity uses terms not typically associated with Christian churches.
    aliases:
    - Non-Christian Terms
  gers_id_already_in_db:
    text: gers_id_already_in_db
    description: The GERS ID already exists in the Global.Church database.
    aliases:
    - GERS ID Already in DB

```
</details>
