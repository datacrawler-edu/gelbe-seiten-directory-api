# Gelbe Seiten Directory API Examples

Search German business listings through a hosted Apify Actor and export the results to CSV.

## What this repository helps you do

Build an integration with [Gelbe Seiten Scraper](https://apify.com/datascraperes/gelbe-seiten-business-directory?fpr=edudata). Look up a trade in a German city, postcode or selected districts and consume one row per unique listing in the run.

## Example result

The fictional [JSON sample](data/sample-output.json) and [CSV sample](data/sample-output.csv) show the Dataset shape. A listing may contain a business name, directory profile, phone, website and address fields.

## Run without code

Open the [hosted Actor](https://apify.com/datascraperes/gelbe-seiten-business-directory?fpr=edudata), enter a trade and city, set a small result limit, and click **Start**. Open **Dataset** when the run finishes and choose CSV or JSON. [No-code guide](docs/no-code-guide.md)

## Try it with Apify's free plan

Check the [Apify plans](https://apify.com/pricing?fpr=edudata) for current included usage. Run the five-result example first to see the fields and estimate your workload.

## Quick start for developers

Set `APIFY_TOKEN` in your shell using your own Apify API token. Run the Python example from the repository root with Python 3.10 or later. It uses the Python standard library.

```sh
python examples/python/search.py
```

## Input example

Use [the sample JSON](data/sample-input.json) for a five-row search. Set `includeDetails` to `true` when you need weekly opening hours. [Input reference](docs/input-reference.md)

## Request examples

- [cURL](examples/curl-request.md) starts a search and shows how to retrieve its Dataset.
- [Python](examples/python/search.py) submits one search. [Batch workflow](examples/python/batch_cities.py) submits one bounded run per city.
- [JavaScript](examples/javascript/request.mjs) submits one search using Node.js 20 or later.

## Output fields

Use `realId` as the identity within the run. Fields include `name`, `profileUrl`, `category`, `street`, `postalCode`, `city`, `phone`, `fax`, `website`, `latitude`, `longitude` and `openingHours`. [Output reference](docs/output-reference.md)

## Common use cases

Compare the same trade across cities, build a supplier shortlist or prepare a spreadsheet of publicly listed opening hours. [Workflow ideas](docs/use-cases.md)

## Run a Gelbe Seiten district search from Python

Set `location` to `Berlin` and `districts` to a list such as `["Mitte", "Wedding"]`. The run processes districts in order and applies one global result limit. A district can fill the limit before the following district is reached.

## Export an existing Gelbe Seiten Dataset to CSV

```sh
python examples/python/export_csv.py DATASET_ID gelbe-seiten.csv
```

Find the Dataset ID in the finished Apify run. This command downloads the existing Dataset without starting a new run.

## FAQ

See [common questions about search scope, hours and costs](docs/faq.md).

## Limits and pricing

The input accepts up to 500 results and 10 districts. Actual coverage depends on the source. The billable event is a unique listing saved. Check the [Actor Pricing tab](https://apify.com/datascraperes/gelbe-seiten-business-directory?fpr=edudata) for current rates.

## Hosted version

[Open Gelbe Seiten Scraper on Apify](https://apify.com/datascraperes/gelbe-seiten-business-directory?fpr=edudata)

## Responsible use

Respect the directory's terms, applicable privacy rules and the purpose for which you collect contact data.

## Support

Use [GitHub Issues](https://github.com/datacrawler-edu/gelbe-seiten-directory-api/issues) for integration examples. Report Actor execution issues in the hosted Actor's Issues tab.

## License

The integration examples are available under the [MIT license](LICENSE).
