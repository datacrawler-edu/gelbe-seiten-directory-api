"""Run the same trade in each city and save the corresponding Dataset IDs."""
import argparse
import json

from common import search

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("keyword")
    parser.add_argument("cities", nargs="+")
    args = parser.parse_args()
    for city in args.cities:
        run = search({"keyword": args.keyword, "location": city, "maxResults": 5})
        print(json.dumps({"city": city, "datasetId": run["defaultDatasetId"]}), flush=True)
