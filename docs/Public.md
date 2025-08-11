# Subset: Public 


_Fields available for public consumption._



URI: [Public](Public.md)



## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema












        


        


        



        


        

        


        

        

        


        

        




        


        


        

        

        

        

        

        

        


        


        

        





        



        

        


        




        

        


        


        






## Classes in subset

| Class | Description |
| --- | --- |
| [Church](Church.md) | A distinct church congregation |
| [EnrichedData](EnrichedData.md) | AI-enriched attributes extracted from the church website and socials |
| [User](User.md) | A registered platform user |


### Slots from [Church](Church.md) also in _public_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [address](address.md) | 0..1 <br/> [String](String.md) | Physical street address  |
| [church_id](church_id.md) | 1 <br/> [Uuid](Uuid.md) | Primary key for Church; referenced by related tables **identifier** |
| [gers_id](gers_id.md) | 0..1 <br/> [String](String.md) | ID from the Government/Ecclesiastical Registry System (if available)  |
| [latitude](latitude.md) | 0..1 <br/> [Float](Float.md) | Geographic latitude (decimal degrees)  |
| [longitude](longitude.md) | 0..1 <br/> [Float](Float.md) | Geographic longitude (decimal degrees)  |
| [name](name.md) | 0..1 <br/> [String](String.md) | Official church name  |

### Slots from [EnrichedData](EnrichedData.md) also in _public_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [belief_type](belief_type.md) | 0..1 <br/> [BeliefTypeEnum](BeliefTypeEnum.md) | Denomination / church type category  |
| [church_beliefs_url](church_beliefs_url.md) | 0..1 <br/> [Uri](Uri.md) | URL of the statement of faith or similar statement of beliefs  |
| [church_id](church_id.md) | 1 <br/> [Uuid](Uuid.md) | Primary key for Church; referenced by related tables **identifier** |
| [church_summary](church_summary.md) | 0..1 <br/> [String](String.md) | Concise summary of the church, including key attributes and offerings  |
| [instagram_url](instagram_url.md) | 0..1 <br/> [Uri](Uri.md) | Instagram profile URL  |
| [programs_offered](programs_offered.md) | 0..1 <br/> [String](String.md) | List of programs or ministries offered  |
| [scraped_address](scraped_address.md) | 0..1 <br/> [String](String.md) | Postal address extracted from site  |
| [service_languages](service_languages.md) | 0..1 <br/> [String](String.md) | Languages in which services are offered  |
| [service_times](service_times.md) | 0..1 <br/> [String](String.md) | Service times (free text)  |
| [trinitarian_beliefs](trinitarian_beliefs.md) | 0..1 <br/> [Boolean](Boolean.md) | True if church affirms classical Trinitarian doctrine  |
| [youtube_url](youtube_url.md) | 0..1 <br/> [Uri](Uri.md) | YouTube channel URL  |

### Slots from [User](User.md) also in _public_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [user_id](user_id.md) | 1 <br/> [Uuid](Uuid.md) | Primary key for User (also referenced by other tables) **identifier** |




## Slots in subset

| Slot | Description |
| --- | --- |
| [address](address.md) | Physical street address |
| [alternate_name](alternate_name.md) | Alternate or colloquial church name |
| [belief_type](belief_type.md) | Denomination / church type category |
| [church_beliefs_url](church_beliefs_url.md) | URL of the statement of faith or similar statement of beliefs |
| [church_id](church_id.md) | Primary key for Church; referenced by related tables |
| [church_summary](church_summary.md) | Concise summary of the church, including key attributes and offerings |
| [country](country.md) | ISO-3166 country code |
| [description](description.md) | Long-form description of the church |
| [gers_id](gers_id.md) | ID from the Government/Ecclesiastical Registry System (if available) |
| [instagram_url](instagram_url.md) | Instagram profile URL |
| [keywords](keywords.md) | Comma-separated keywords or tags |
| [latitude](latitude.md) | Geographic latitude (decimal degrees) |
| [locality](locality.md) | City or locality of the church |
| [longitude](longitude.md) | Geographic longitude (decimal degrees) |
| [name](name.md) | Official church name |
| [opening_hours](opening_hours.md) | Opening hours information |
| [phone](phone.md) | Church phone number |
| [postal_code](postal_code.md) | Postal / ZIP code |
| [programs_offered](programs_offered.md) | List of programs or ministries offered |
| [region](region.md) | State, province, or region |
| [scraped_address](scraped_address.md) | Postal address extracted from site |
| [service_languages](service_languages.md) | Languages in which services are offered |
| [service_times](service_times.md) | Service times (free text) |
| [social_media](social_media.md) | JSON or comma-separated social media handles |
| [trinitarian_beliefs](trinitarian_beliefs.md) | True if church affirms classical Trinitarian doctrine |
| [user_id](user_id.md) | Primary key for User (also referenced by other tables) |
| [website](website.md) | Full website URL |
| [youtube_url](youtube_url.md) | YouTube channel URL |


