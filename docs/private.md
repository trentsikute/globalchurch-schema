# Subset: private 


_Fields available with proper permissions._



URI: [Private](Private.md)




## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema













        


        




        









        

        

        


        


        








        












        




        


        











## Classes in subset

| Class | Description |
| --- | --- |
| [ChurchWebsiteText](ChurchWebsiteText.md) | Raw scrape artifacts captured from the church root URL |
| [User](User.md) | A registered platform user |



### Slots from [User](User.md) also in _private_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [alternate_church](alternate_church.md) | 0..1 <br/> [String](String.md) | Optional FK to a secondary/alternate Church  |
| [email](email.md) | 0..1 <br/> [email](email.md) | Primary contact email for the user  |
| [faith_journey](faith_journey.md) | 0..1 <br/> [String](String.md) | Narrative of the user’s faith journey  |
| [family_name](family_name.md) | 0..1 <br/> [String](String.md) | User’s last (family) name  |
| [given_name](given_name.md) | 0..1 <br/> [String](String.md) | User’s first (given) name  |
| [interests](interests.md) | 0..1 <br/> [String](String.md) | User’s interests or ministry areas  |
| [primary_church](primary_church.md) | 0..1 <br/> [Uuid](Uuid.md) | FK to the user’s primary Church  |
| [skills](skills.md) | * <br/> [String](String.md) | List of user skills  |
| [telephone](telephone.md) | 0..1 <br/> [PhoneE164](PhoneE164.md) | User’s phone number (E  |
| [user_id](user_id.md) | 1 <br/> [Uuid](Uuid.md) | Unique ID for a registered platform user **identifier** |





## Slots in subset

| Slot | Description |
| --- | --- |
| [alternate_church](alternate_church.md) | Optional FK to a secondary/alternate Church |
| [email](email.md) | Primary contact email for the user |
| [faith_journey](faith_journey.md) | Narrative of the user’s faith journey |
| [family_name](family_name.md) | User’s last (family) name |
| [given_name](given_name.md) | User’s first (given) name |
| [interests](interests.md) | User’s interests or ministry areas |
| [primary_church](primary_church.md) | FK to the user’s primary Church |
| [skills](skills.md) | List of user skills |
| [telephone](telephone.md) | User’s phone number (E |
| [user_id](user_id.md) | Unique ID for a registered platform user |



