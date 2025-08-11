# Subset: Enrichment 


_Usually derived by AI or post-processing._



URI: [Enrichment](Enrichment.md)



## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema














        








        


        


        



        






        








        




        






        

        


        

        


        




        





        






## Classes in subset

| Class | Description |
| --- | --- |
| [EnrichedData](EnrichedData.md) | AI-enriched attributes extracted from the church website and socials |


### Slots from [EnrichedData](EnrichedData.md) also in _enrichment_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [belief_type](belief_type.md) | 0..1 <br/> [BeliefTypeEnum](BeliefTypeEnum.md) | Denomination / church type category  |
| [church_beliefs_url](church_beliefs_url.md) | 0..1 <br/> [Uri](Uri.md) | URL of the statement of faith or similar statement of beliefs  |
| [church_summary](church_summary.md) | 0..1 <br/> [String](String.md) | Concise summary of the church, including key attributes and offerings  |
| [instagram_url](instagram_url.md) | 0..1 <br/> [Uri](Uri.md) | Instagram profile URL  |
| [programs_offered](programs_offered.md) | 0..1 <br/> [String](String.md) | List of programs or ministries offered  |
| [scraped_address](scraped_address.md) | 0..1 <br/> [String](String.md) | Postal address extracted from site  |
| [scraped_email](scraped_email.md) | 0..1 <br/> [email](email.md) | Email address extracted from site  |
| [service_languages](service_languages.md) | 0..1 <br/> [String](String.md) | Languages in which services are offered  |
| [service_times](service_times.md) | 0..1 <br/> [String](String.md) | Service times (free text)  |
| [trinitarian_beliefs](trinitarian_beliefs.md) | 0..1 <br/> [Boolean](Boolean.md) | True if church affirms classical Trinitarian doctrine  |
| [youtube_url](youtube_url.md) | 0..1 <br/> [Uri](Uri.md) | YouTube channel URL  |




## Slots in subset

| Slot | Description |
| --- | --- |
| [belief_type](belief_type.md) | Denomination / church type category |
| [church_beliefs_url](church_beliefs_url.md) | URL of the statement of faith or similar statement of beliefs |
| [church_summary](church_summary.md) | Concise summary of the church, including key attributes and offerings |
| [description](description.md) | Long-form description of the church |
| [instagram_url](instagram_url.md) | Instagram profile URL |
| [phone](phone.md) | Church phone number |
| [programs_offered](programs_offered.md) | List of programs or ministries offered |
| [scraped_address](scraped_address.md) | Postal address extracted from site |
| [scraped_email](scraped_email.md) | Email address extracted from site |
| [service_languages](service_languages.md) | Languages in which services are offered |
| [service_times](service_times.md) | Service times (free text) |
| [social_media](social_media.md) | JSON or comma-separated social media handles |
| [trinitarian_beliefs](trinitarian_beliefs.md) | True if church affirms classical Trinitarian doctrine |
| [youtube_url](youtube_url.md) | YouTube channel URL |


