# Global.Church Schema

The shared data model for Global.Church and partner projects, defining core classes (Church, User) and slots for ingestion, enrichment, and publishing.


URI: https://global.church/schema

Name: Global.Church-schema



## Classes

| Class | Description |
| --- | --- |
| [Church](Church.md) | A distinct church congregation |
| [ChurchWebsiteText](ChurchWebsiteText.md) | Raw scrape artifacts captured from the church root URL |
| [Overture](Overture.md) | Original place record as supplied by Overture Maps |
| [User](User.md) | A registered platform user |



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
| pii | Potentially personally identifiable or sensitive. |
| private | Fields available with proper permissions. |
| public | Fields available for public consumption. |
| user_core | Minimal fields needed to represent a user. |
