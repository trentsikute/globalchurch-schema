

# Class: Overture 


_Original place record as supplied by Overture Maps._





URI: [gc:Overture](https://global.church/schema/Overture)











<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [gers_id](gers_id.md) | 1 <br/> [String](String.md) | Government/Ecclesiastical Registry System identifier | direct |
| [version](version.md) | 0..1 <br/> [Integer](Integer.md) | Overture dataset version number | direct |
| [source](source.md) | 0..1 <br/> [String](String.md) | Source label from Overture Maps | direct |
| [confidence](confidence.md) | 0..1 <br/> [Float](Float.md) | Confidence score (0–1) from Overture | direct |
| [source_release](source_release.md) | 0..1 <br/> [Date](Date.md) | Overture release tag (YYYY-MM-DD) | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://global.church/schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gc:Overture |
| native | gc:Overture |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Overture
description: Original place record as supplied by Overture Maps.
in_subset:
- overture
- internal
- public
from_schema: https://global.church/schema
rank: 1000
slots:
- gers_id
- version
- source
- confidence
- source_release

```
</details>

### Induced

<details>
```yaml
name: Overture
description: Original place record as supplied by Overture Maps.
in_subset:
- overture
- internal
- public
from_schema: https://global.church/schema
rank: 1000
attributes:
  gers_id:
    name: gers_id
    description: Government/Ecclesiastical Registry System identifier.
    comments:
    - 'External registry identifier used for cross-referencing with official listings.

      May not exist for all churches.

      '
    examples:
    - value: GERS-CA-00012345
      description: Sample registry ID.
    in_subset:
    - overture
    - public
    from_schema: https://global.church/schema
    rank: 1000
    identifier: true
    alias: gers_id
    owner: Overture
    domain_of:
    - Church
    - Overture
    range: string
    required: true
  version:
    name: version
    description: Overture dataset version number.
    comments:
    - 'Integer version tag from the Overture Maps release metadata.

      Use with `source_release` when available.

      '
    examples:
    - value: '13'
      description: Example Overture version.
    in_subset:
    - overture
    from_schema: https://global.church/schema
    rank: 1000
    alias: version
    owner: Overture
    domain_of:
    - Overture
    range: integer
  source:
    name: source
    description: Source label from Overture Maps.
    comments:
    - 'The upstream source name (e.g., “overture_places”, “overture_poi”).

      Helps with lineage and debugging.

      '
    examples:
    - value: overture_places
      description: Upstream dataset label.
    in_subset:
    - overture
    from_schema: https://global.church/schema
    rank: 1000
    alias: source
    owner: Overture
    domain_of:
    - Overture
    range: string
  confidence:
    name: confidence
    description: Confidence score (0–1) from Overture.
    comments:
    - 'A numeric score indicating confidence in the match or attribution.

      If absent upstream, leave empty rather than inventing a value.

      '
    examples:
    - value: '0.92'
      description: High-confidence attribution.
    in_subset:
    - overture
    from_schema: https://global.church/schema
    rank: 1000
    alias: confidence
    owner: Overture
    domain_of:
    - Overture
    range: float
  source_release:
    name: source_release
    description: Overture release tag (YYYY-MM-DD).
    comments:
    - 'The official release date string from Overture (e.g., 2024-05-15).

      Use ISO 8601 date format.

      '
    examples:
    - value: '2024-05-15'
      description: Release date.
    in_subset:
    - overture
    from_schema: https://global.church/schema
    rank: 1000
    alias: source_release
    owner: Overture
    domain_of:
    - Overture
    range: date

```
</details>