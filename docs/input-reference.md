# Input reference

| Key | Type | Behavior |
| --- | --- | --- |
| `keyword` | string | Required trade or business name, 1–100 characters. |
| `location` | string | Required German city or postcode, 1–100 characters. |
| `maxResults` | integer | Optional cap of 1–500 unique listings. Defaults to 100. |
| `includeDetails` | boolean | Optional full weekly opening hours. Defaults to false. |
| `districts` | array of strings | Optional list of up to 10 districts. Use a city for location. |

Use the [sample input](../data/sample-input.json) as a starting point. Districts are processed in order and share the cap.
