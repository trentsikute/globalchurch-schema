# Subset: internal 


_Operational/internal fields for Global.Church._



URI: [Internal](Internal.md)




## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema













        

        







        



















        





        

        

        

        


        

        







        





        








## Classes in subset

| Class | Description |
| --- | --- |
| [ChurchWebsiteText](ChurchWebsiteText.md) | Raw scrape artifacts captured from the church root URL |
| [Overture](Overture.md) | Original place record as supplied by Overture Maps |


### Slots from [ChurchWebsiteText](ChurchWebsiteText.md) also in _internal_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [candidates_text_and_links](candidates_text_and_links.md) | * <br/> [String](String.md) | Text snippets and associated links for candidate pages  |
| [root_candidates](root_candidates.md) | * <br/> [String](String.md) | Candidate URLs extracted from the root page  |
| [root_scrape_buttons](root_scrape_buttons.md) | 0..1 <br/> [String](String.md) | Button texts captured on the root page  |
| [root_scrape_check](root_scrape_check.md) | 0..1 <br/> [String](String.md) | Checksum or status flag indicating scrape state  |
| [root_scrape_text](root_scrape_text.md) | 0..1 <br/> [String](String.md) | Visible text content scraped from the website root page  |






## Slots in subset

| Slot | Description |
| --- | --- |
| [candidates_text_and_links](candidates_text_and_links.md) | Text snippets and associated links for candidate pages |
| [pipeline_status](pipeline_status.md) | Current enrichment pipeline stage |
| [root_candidates](root_candidates.md) | Candidate URLs extracted from the root page |
| [root_scrape_buttons](root_scrape_buttons.md) | Button texts captured on the root page |
| [root_scrape_check](root_scrape_check.md) | Checksum or status flag indicating scrape state |
| [root_scrape_text](root_scrape_text.md) | Visible text content scraped from the website root page |
| [scraped_email](scraped_email.md) | Public email address extracted from the website |
| [search_blob](search_blob.md) | Concatenated text of searchable fields for indexing |
| [telephone](telephone.md) | User’s phone number (E |
| [website_root](website_root.md) | Root URL of the church website (scheme and domain only) |



