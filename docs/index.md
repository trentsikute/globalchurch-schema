# GlobalChurch



URI: https://global.church/schema

Name: GlobalChurch



## Classes

| Class | Description |
| --- | --- |
| [Church](Church.md) | A distinct church congregation |
| [User](User.md) | A registered platform user |



## Slots

| Slot | Description |
| --- | --- |
| [address](address.md) | Physical street address |
| [alternate_church](alternate_church.md) | Optional FK → Church |
| [church_id](church_id.md) | Primary key for Church; referenced by related tables |
| [email](email.md) | Main contact email |
| [faith_journey](faith_journey.md) | Narrative text describing the user’s faith journey |
| [family_name](family_name.md) | Last name |
| [gers_id](gers_id.md) | ID from the Government/Ecclesiastical Registry System (if available) |
| [given_name](given_name.md) | First name |
| [interests](interests.md) | Free-text interests or ministry areas |
| [latitude](latitude.md) | Geographic latitude (decimal degrees) |
| [longitude](longitude.md) | Geographic longitude (decimal degrees) |
| [name](name.md) | Official church name |
| [pipeline_status](pipeline_status.md) | Enrichment pipeline stage (e |
| [primary_church](primary_church.md) | FK → Church |
| [skills](skills.md) | Comma-separated list of user skills |
| [telephone](telephone.md) | Phone number (international format recommended) |
| [user_id](user_id.md) | Primary key for User (also referenced by other tables) |


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
