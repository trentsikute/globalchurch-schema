# Global Church Schema

The shared data model for Global.Church and partner projects, defining core classes (Church, User) and slots for ingestion, enrichment, and publishing.


URI: https://global.church/schema

Name: GlobalChurch-schema



## Classes

| Class | Description |
| --- | --- |
| [Church](Church.md) | A distinct church congregation |
| [ChurchWebsite](ChurchWebsite.md) | Raw scrape artifacts captured from the church root URL |
| [EnrichedData](EnrichedData.md) | AI-enriched attributes extracted from the church website and socials |
| [Overture](Overture.md) | Original place record as supplied by Overture Maps |
| [User](User.md) | A registered platform user |



## Slots

| Slot | Description |
| --- | --- |
| [address](address.md) | Physical street address of the church or user |
| [alternate_church](alternate_church.md) | Optional FK to a secondary/alternate Church |
| [alternate_name](alternate_name.md) | Alternate, colloquial, or short name for the church |
| [belief_type](belief_type.md) | Denomination / church type category |
| [candidates_text_and_links](candidates_text_and_links.md) | Text snippets and associated links for candidate pages |
| [church_beliefs_url](church_beliefs_url.md) | URL for the church’s statement of beliefs/faith |
| [church_id](church_id.md) | Global |
| [church_summary](church_summary.md) | Concise public summary of the church |
| [confidence](confidence.md) | Confidence score (0–1) from Overture |
| [country](country.md) | Country code in ISO 3166-1 alpha-2 format |
| [description](description.md) | Detailed narrative description of the church |
| [email](email.md) | Primary contact email for the user |
| [faith_journey](faith_journey.md) | Narrative of the user’s faith journey |
| [family_name](family_name.md) | User’s last (family) name |
| [gers_id](gers_id.md) | Government/Ecclesiastical Registry System identifier |
| [given_name](given_name.md) | User’s first (given) name |
| [instagram_url](instagram_url.md) | Instagram profile URL |
| [interests](interests.md) | User’s interests or ministry areas |
| [keywords](keywords.md) | Keywords or tags describing the church |
| [latitude](latitude.md) | Latitude in decimal degrees |
| [locality](locality.md) | City or locality where the church is located |
| [longitude](longitude.md) | Longitude in decimal degrees |
| [name](name.md) | Official church name |
| [opening_hours](opening_hours.md) | Church opening hours or service schedule |
| [phone](phone.md) | Official phone number for the church |
| [pipeline_status](pipeline_status.md) | Current enrichment pipeline stage |
| [postal_code](postal_code.md) | Postal code or ZIP code for the address |
| [primary_church](primary_church.md) | FK to the user’s primary Church |
| [programs_offered](programs_offered.md) | Programs or ministries the church offers |
| [region](region.md) | State, province, or administrative region |
| [root_candidates](root_candidates.md) | Candidate URLs extracted from the root page |
| [root_scrape_buttons](root_scrape_buttons.md) | Button texts captured on the root page |
| [root_scrape_check](root_scrape_check.md) | Checksum or status flag indicating scrape state |
| [root_scrape_text](root_scrape_text.md) | Visible text content scraped from the website root page |
| [scraped_address](scraped_address.md) | Postal address extracted from the website |
| [scraped_email](scraped_email.md) | Public email address extracted from the website |
| [search_blob](search_blob.md) | Concatenated text of searchable fields for indexing |
| [service_languages](service_languages.md) | Languages in which services are offered |
| [service_times](service_times.md) | Service times for public gatherings |
| [skills](skills.md) | List of user skills |
| [social_media](social_media.md) | List of social media handles or URLs associated with the church |
| [source](source.md) | Source label from Overture Maps |
| [source_release](source_release.md) | Overture release tag (YYYY-MM-DD) |
| [telephone](telephone.md) | User’s phone number (E |
| [trinitarian_beliefs](trinitarian_beliefs.md) | Whether the church affirms classical Trinitarian doctrine |
| [user_id](user_id.md) | Unique ID for a registered platform user |
| [version](version.md) | Overture dataset version number |
| [website](website.md) | Full website URL for the church |
| [website_root](website_root.md) | Root URL of the church website (scheme and domain only) |
| [youtube_url](youtube_url.md) | YouTube channel URL |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [BeliefTypeEnum](BeliefTypeEnum.html) | Top-level Christian family grouping used by Global |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Email](Email.md) | Email address (simplified RFC 5322) |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [IsoCountryCode](IsoCountryCode.md) | ISO 3166-1 alpha-2 country code |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [PhoneE164](PhoneE164.md) | Telephone number in E |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |
| [Uuid](Uuid.md) | Universally unique identifier (RFC 4122) |

## Subsets

| Subset | Description |
| --- | --- |
| church_core | Minimal fields needed to represent a church. |
| enrichment | Usually derived by AI or post-processing. |
| internal | Operational/internal fields for Global.Church. |
| overture | Sourced from Overture Maps. |
| pii | Potentially personally identifiable or sensitive. |
| public | Fields available for public consumption. |
| user_core | Minimal fields needed to represent a user. |
