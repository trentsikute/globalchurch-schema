# GlobalChurch



URI: https://global.church/schema

Name: GlobalChurch



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
| [address](address.md) | Physical street address |
| [alternate_church](alternate_church.md) | Optional FK → Church |
| [alternateName](alternateName.md) | Alternate or colloquial church name |
| [belief_type](belief_type.md) | Denomination / church type category |
| [candidates_text_and_links](candidates_text_and_links.md) | Text and associated links for candidate pages |
| [church_beliefs_url](church_beliefs_url.md) | URL of the statement of faith or similar statement of beliefs |
| [church_id](church_id.md) | Primary key for Church; referenced by related tables |
| [church_summary](church_summary.md) | Concise summary of the church, including key attributes and offerings |
| [confidence](confidence.md) | Confidence score (0–1) |
| [country](country.md) | ISO-3166 country code |
| [description](description.md) | Long-form description of the church |
| [email](email.md) | Main contact email |
| [faith_journey](faith_journey.md) | Narrative text describing the user’s faith journey |
| [family_name](family_name.md) | Last name |
| [gers_id](gers_id.md) | ID from the Government/Ecclesiastical Registry System (if available) |
| [given_name](given_name.md) | First name |
| [instagram_url](instagram_url.md) | Instagram profile URL |
| [interests](interests.md) | Free-text interests or ministry areas |
| [keywords](keywords.md) | Comma-separated keywords or tags |
| [latitude](latitude.md) | Geographic latitude (decimal degrees) |
| [locality](locality.md) | City or locality of the church |
| [longitude](longitude.md) | Geographic longitude (decimal degrees) |
| [name](name.md) | Official church name |
| [openingHours](openingHours.md) | Opening hours information |
| [phone](phone.md) | Church phone number |
| [pipeline_status](pipeline_status.md) | Enrichment pipeline stage (e |
| [postal_code](postal_code.md) | Postal / ZIP code |
| [primary_church](primary_church.md) | FK → Church |
| [programs_offered](programs_offered.md) | List of programs or ministries offered |
| [region](region.md) | State, province, or region |
| [root_candidates](root_candidates.md) | Candidate URLs extracted from the root page |
| [root_scrape_buttons](root_scrape_buttons.md) | Button texts captured on root page |
| [root_scrape_check](root_scrape_check.md) | Checksum or status flag of the scrape |
| [root_scrape_text](root_scrape_text.md) | Visible text scraped from the root page |
| [scraped_address](scraped_address.md) | Postal address extracted from site |
| [scraped_email](scraped_email.md) | Email address extracted from site |
| [search_blob](search_blob.md) | Concatenated text blob used for full-text search |
| [service_languages](service_languages.md) | Languages in which services are offered |
| [service_times](service_times.md) | Service times (free text) |
| [skills](skills.md) | Comma-separated list of user skills |
| [social_media](social_media.md) | JSON or comma-separated social media handles |
| [source](source.md) | Source label of the Overture record |
| [source_release](source_release.md) | Overture release tag (e |
| [telephone](telephone.md) | Phone number (international format recommended) |
| [trinitarian_beliefs](trinitarian_beliefs.md) | True if church affirms classical Trinitarian doctrine |
| [user_id](user_id.md) | Primary key for User (also referenced by other tables) |
| [version](version.md) | Overture version number |
| [website](website.md) | Full website URL |
| [website_root](website_root.md) | Root URL (scheme + domain) |
| [youtube_url](youtube_url.md) | YouTube channel URL |


## Enumerations

| Enumeration | Description |
| --- | --- |


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
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |
| [Uuid](Uuid.md) | Universally unique identifier (RFC 4122) |


## Subsets

| Subset | Description |
| --- | --- |
