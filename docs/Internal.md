# Subset: Internal 


_Operational/internal fields for Global.Church._



URI: [Internal](Internal.md)



## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema













        







        



        







        

        





        








        


        



        

        

        

        


        

        



        




        





        







## Classes in subset

| Class | Description |
| --- | --- |
| [ChurchWebsite](ChurchWebsite.md) | Raw scrape artifacts captured from the church root URL |


### Slots from [ChurchWebsite](ChurchWebsite.md) also in _internal_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [candidates_text_and_links](candidates_text_and_links.md) | 0..1 <br/> [String](String.md) | Text and associated links for candidate pages  |
| [root_candidates](root_candidates.md) | 0..1 <br/> [String](String.md) | Candidate URLs extracted from the root page  |
| [root_scrape_buttons](root_scrape_buttons.md) | 0..1 <br/> [String](String.md) | Button texts captured on root page  |
| [root_scrape_check](root_scrape_check.md) | 0..1 <br/> [String](String.md) | Checksum or status flag of the scrape  |
| [root_scrape_text](root_scrape_text.md) | 0..1 <br/> [String](String.md) | Visible text scraped from the root page  |




## Slots in subset

| Slot | Description |
| --- | --- |
| [alternate_church](alternate_church.md) | Optional FK → Church |
| [candidates_text_and_links](candidates_text_and_links.md) | Text and associated links for candidate pages |
| [email](email.md) | Main contact email |
| [faith_journey](faith_journey.md) | Narrative text describing the user’s faith journey |
| [interests](interests.md) | Free-text interests or ministry areas |
| [pipeline_status](pipeline_status.md) | Enrichment pipeline stage (e |
| [primary_church](primary_church.md) | FK → Church |
| [root_candidates](root_candidates.md) | Candidate URLs extracted from the root page |
| [root_scrape_buttons](root_scrape_buttons.md) | Button texts captured on root page |
| [root_scrape_check](root_scrape_check.md) | Checksum or status flag of the scrape |
| [root_scrape_text](root_scrape_text.md) | Visible text scraped from the root page |
| [scraped_email](scraped_email.md) | Email address extracted from site |
| [search_blob](search_blob.md) | Concatenated text blob used for full-text search |
| [skills](skills.md) | Comma-separated list of user skills |
| [telephone](telephone.md) | Phone number (international format recommended) |
| [website_root](website_root.md) | Root URL (scheme + domain) |


