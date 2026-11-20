# Output reference

- Identity: `realId`, `name`, `profileUrl`.
- Classification and location: `category`, `street`, `postalCode`, `city`.
- Contact and map details: `phone`, `fax`, `website`, `latitude`, `longitude`.
- Schedule: `openingHours`, a list of strings. An empty list can mean the details option was disabled or hours were unavailable.

Unpublished optional fields can be null. Read the `SUMMARY` record alongside the Dataset when a run stops early. See [sample JSON](../data/sample-output.json).
