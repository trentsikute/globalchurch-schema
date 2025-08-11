# Subset: UserCore 


_Minimal fields needed to represent a user._



URI: [UserCore](UserCore.md)



## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema
















        














        


        


        






























        










## Classes in subset

| Class | Description |
| --- | --- |
| [User](User.md) | A registered platform user |


### Slots from [User](User.md) also in _user_core_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [email](email.md) | 0..1 <br/> [email](email.md) | Main contact email  |
| [family_name](family_name.md) | 0..1 <br/> [String](String.md) | Last name  |
| [given_name](given_name.md) | 0..1 <br/> [String](String.md) | First name  |
| [user_id](user_id.md) | 1 <br/> [Uuid](Uuid.md) | Primary key for User (also referenced by other tables) **identifier** |




## Slots in subset

| Slot | Description |
| --- | --- |
| [email](email.md) | Main contact email |
| [family_name](family_name.md) | Last name |
| [given_name](given_name.md) | First name |
| [user_id](user_id.md) | Primary key for User (also referenced by other tables) |


