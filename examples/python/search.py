"""Start one small Gelbe Seiten search and read its Dataset."""
import json
from pathlib import Path

from common import request, search

if __name__ == "__main__":
    payload = json.loads((Path(__file__).resolve().parents[2] / "data/sample-input.json").read_text())
    run = search(payload)
    print(json.dumps(json.loads(request(f"datasets/{run['defaultDatasetId']}/items")), indent=2))
