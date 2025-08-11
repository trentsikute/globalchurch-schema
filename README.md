# GlobalChurch Schema

This project defines the LinkML schema for Global.Church, including classes, slots, enumerations, and mappings to schema.org.

## Getting Started

The schema is written in LinkML YAML format. It is recommended to use a Python virtual environment to manage dependencies and tools.

## Schema.org Alignment

The schema is designed to align closely with the Schema.org vocabulary to ensure maximum interoperability. Many classes and slots include `mappings` or `exact_mappings` to Schema.org terms, allowing other systems and search engines to easily interpret the data. Additionally, the `context.jsonld` file generated from the schema incorporates these Schema.org mappings, facilitating Linked Data consumption.

## License

License information will be placed here when available.