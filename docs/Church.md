

# Class: Church 


_A distinct church congregation._





URI: [gc:Church](https://global.church/schema/Church)





```mermaid
 classDiagram
    class Church
    click Church href "../Church/"
      Church : address
        
      Church : church_id
        
      Church : gers_id
        
      Church : latitude
        
      Church : longitude
        
      Church : name
        
      Church : pipeline_status
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [church_id](church_id.md) | 1 <br/> [Uuid](Uuid.md) | Primary key for Church; referenced by related tables | direct |
| [gers_id](gers_id.md) | 0..1 <br/> [String](String.md) | ID from the Government/Ecclesiastical Registry System (if available) | direct |
| [name](name.md) | 0..1 <br/> [String](String.md) | Official church name | direct |
| [pipeline_status](pipeline_status.md) | 0..1 <br/> [String](String.md) | Enrichment pipeline stage (e | direct |
| [latitude](latitude.md) | 0..1 <br/> [Float](Float.md) | Geographic latitude (decimal degrees) | direct |
| [longitude](longitude.md) | 0..1 <br/> [Float](Float.md) | Geographic longitude (decimal degrees) | direct |
| [address](address.md) | 0..1 <br/> [String](String.md) | Physical street address | direct |










## Identifier and Mapping Information






### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:Church |
| native | gc:Church |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Church
description: A distinct church congregation.
from_schema: https://global.church/schema
slots:
- church_id
- gers_id
- name
- pipeline_status
- latitude
- longitude
- address

```
</details>

### Induced

<details>
```yaml
name: Church
description: A distinct church congregation.
from_schema: https://global.church/schema
attributes:
  church_id:
    name: church_id
    description: Primary key for Church; referenced by related tables.
    from_schema: https://global.church/schema
    rank: 1000
    identifier: true
    alias: church_id
    owner: Church
    domain_of:
    - Church
    range: uuid
    required: true
  gers_id:
    name: gers_id
    description: ID from the Government/Ecclesiastical Registry System (if available).
    from_schema: https://global.church/schema
    rank: 1000
    alias: gers_id
    owner: Church
    domain_of:
    - Church
    range: string
  name:
    name: name
    description: Official church name.
    from_schema: https://global.church/schema
    exact_mappings:
    - schema:name
    rank: 1000
    alias: name
    owner: Church
    domain_of:
    - Church
    range: string
  pipeline_status:
    name: pipeline_status
    description: Enrichment pipeline stage (e.g., RAW, CLEAN, ENRICHED, VALIDATED).
    from_schema: https://global.church/schema
    rank: 1000
    alias: pipeline_status
    owner: Church
    domain_of:
    - Church
    range: string
  latitude:
    name: latitude
    description: Geographic latitude (decimal degrees).
    from_schema: https://global.church/schema
    rank: 1000
    alias: latitude
    owner: Church
    domain_of:
    - Church
    range: float
  longitude:
    name: longitude
    description: Geographic longitude (decimal degrees).
    from_schema: https://global.church/schema
    rank: 1000
    alias: longitude
    owner: Church
    domain_of:
    - Church
    range: float
  address:
    name: address
    description: Physical street address.
    from_schema: https://global.church/schema
    rank: 1000
    alias: address
    owner: Church
    domain_of:
    - Church
    range: string

```
</details>