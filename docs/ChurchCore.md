# Subset: ChurchCore 


_Minimal fields needed to represent a church._



URI: [ChurchCore](ChurchCore.md)



## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema












        







        






        



        










        

        

        

        




        



        


























## Classes in subset

| Class | Description |
| --- | --- |
| [Church](Church.md) | A distinct church congregation |


### Slots from [Church](Church.md) also in _church_core_

| Name | Cardinality and Range | Description |
| ---  | ---  | --- |
| [address](address.md) | 0..1 <br/> [String](String.md) | Physical street address  |
| [church_id](church_id.md) | 1 <br/> [Uuid](Uuid.md) | Primary key for Church; referenced by related tables **identifier** |
| [latitude](latitude.md) | 0..1 <br/> [Float](Float.md) | Geographic latitude (decimal degrees)  |
| [longitude](longitude.md) | 0..1 <br/> [Float](Float.md) | Geographic longitude (decimal degrees)  |
| [name](name.md) | 0..1 <br/> [String](String.md) | Official church name  |




## Slots in subset

| Slot | Description |
| --- | --- |
| [address](address.md) | Physical street address |
| [church_id](church_id.md) | Primary key for Church; referenced by related tables |
| [country](country.md) | ISO-3166 country code |
| [latitude](latitude.md) | Geographic latitude (decimal degrees) |
| [locality](locality.md) | City or locality of the church |
| [longitude](longitude.md) | Geographic longitude (decimal degrees) |
| [name](name.md) | Official church name |
| [postal_code](postal_code.md) | Postal / ZIP code |
| [region](region.md) | State, province, or region |


