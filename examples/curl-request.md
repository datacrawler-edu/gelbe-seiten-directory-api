# Start a search with cURL

Set `APIFY_TOKEN` in your environment and run from the repository root.

```sh
curl --fail-with-body --max-time 100 --request POST   --header "Authorization: Bearer $APIFY_TOKEN"   --header "Content-Type: application/json"   --data-binary @data/sample-input.json   'https://api.apify.com/v2/acts/datascraperes~gelbe-seiten-business-directory/runs?waitForFinish=60&timeout=90&maxTotalChargeUsd=0.05'
```

If the response status is `SUCCEEDED`, copy `data.defaultDatasetId` into the following command. If the start timed out, inspect the Apify Console before submitting again.

```sh
curl --fail-with-body --max-time 30   --header "Authorization: Bearer $APIFY_TOKEN"   'https://api.apify.com/v2/datasets/DATASET_ID/items?format=csv'   --output gelbe-seiten.csv
```
