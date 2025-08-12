# Subset: public 


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
| [address](address.md) | 0..1 <br/> [String](String.md) | Physical street address of the church or user  |
| [church_id](church_id.md) | 1 <br/> [Uuid](Uuid.md) | Global **identifier** |
| [country](country.md) | 1 <br/> [IsoCountryCode](IsoCountryCode.md) | Country code in ISO 3166-1 alpha-2 format  |
| [gers_id](gers_id.md) | 0..1 <br/> [String](String.md) | Government/Ecclesiastical Registry System identifier  |
| [latitude](latitude.md) | 0..1 <br/> [Float](Float.md) | Latitude in decimal degrees  |
| [locality](locality.md) | 0..1 <br/> [String](String.md) | City or locality where the church is located  |
| [longitude](longitude.md) | 0..1 <br/> [Float](Float.md) | Longitude in decimal degrees  |
| [name](name.md) | 1 <br/> [String](String.md) | Official church name  |
| [postal_code](postal_code.md) | 0..1 <br/> [String](String.md) | Postal code or ZIP code for the address  |
| [region](region.md) | 0..1 <br/> [String](String.md) | State, province, or administrative region  |

### Slots from [EnrichedData](EnrichedData.md) also in _public_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [belief_type](belief_type.md) | 0..1 <br/> [BeliefTypeEnum](BeliefTypeEnum.md) | Denomination / church type category  |
| [church_beliefs_url](church_beliefs_url.md) | 0..1 <br/> [Uri](Uri.md) | URL for the church’s statement of beliefs/faith  |
| [church_id](church_id.md) | 1 <br/> [Uuid](Uuid.md) | Global **identifier** |
| [church_summary](church_summary.md) | 0..1 <br/> [String](String.md) | Concise public summary of the church  |
| [instagram_url](instagram_url.md) | 0..1 <br/> [Uri](Uri.md) | Instagram profile URL  |
| [programs_offered](programs_offered.md) | * <br/> [String](String.md) | Programs or ministries the church offers  |
| [scraped_address](scraped_address.md) | 0..1 <br/> [String](String.md) | Postal address extracted from the website  |
| [service_languages](service_languages.md) | * <br/> [String](String.md) | Languages in which services are offered  |
| [service_times](service_times.md) | 0..1 <br/> [String](String.md) | Service times for public gatherings  |
| [trinitarian_beliefs](trinitarian_beliefs.md) | 0..1 <br/> [Boolean](Boolean.md) | Whether the church affirms classical Trinitarian doctrine  |
| [youtube_url](youtube_url.md) | 0..1 <br/> [Uri](Uri.md) | YouTube channel URL  |





## Slots in subset

| Slot | Description |
| --- | --- |
| [address](address.md) | Physical street address of the church or user |
| [alternate_name](alternate_name.md) | Alternate, colloquial, or short name for the church |
| [belief_type](belief_type.md) | Denomination / church type category |
| [church_beliefs_url](church_beliefs_url.md) | URL for the church’s statement of beliefs/faith |
| [church_id](church_id.md) | Global |
| [church_summary](church_summary.md) | Concise public summary of the church |
| [country](country.md) | Country code in ISO 3166-1 alpha-2 format |
| [description](description.md) | Detailed narrative description of the church |
| [gers_id](gers_id.md) | Government/Ecclesiastical Registry System identifier |
| [instagram_url](instagram_url.md) | Instagram profile URL |
| [keywords](keywords.md) | Keywords or tags describing the church |
| [latitude](latitude.md) | Latitude in decimal degrees |
| [locality](locality.md) | City or locality where the church is located |
| [longitude](longitude.md) | Longitude in decimal degrees |
| [name](name.md) | Official church name |
| [opening_hours](opening_hours.md) | Church opening hours or service schedule |
| [phone](phone.md) | Official phone number for the church |
| [postal_code](postal_code.md) | Postal code or ZIP code for the address |
| [programs_offered](programs_offered.md) | Programs or ministries the church offers |
| [region](region.md) | State, province, or administrative region |
| [scraped_address](scraped_address.md) | Postal address extracted from the website |
| [service_languages](service_languages.md) | Languages in which services are offered |
| [service_times](service_times.md) | Service times for public gatherings |
| [social_media](social_media.md) | List of social media handles or URLs associated with the church |
| [trinitarian_beliefs](trinitarian_beliefs.md) | Whether the church affirms classical Trinitarian doctrine |
| [website](website.md) | Full website URL for the church |
| [youtube_url](youtube_url.md) | YouTube channel URL |


