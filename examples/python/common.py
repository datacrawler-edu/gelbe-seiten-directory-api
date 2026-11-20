"""Small HTTP helpers for the hosted Apify Actor."""
import json
import os
from urllib.request import Request, urlopen

BASE = "https://api.apify.com/v2"
ACTOR = "datascraperes~gelbe-seiten-business-directory"


def request(path, *, body=None):
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_TOKEN first.")
    data = json.dumps(body).encode() if body is not None else None
    req = Request(f"{BASE}/{path}", data=data, headers={
        "Authorization": f"Bearer {token}", "Content-Type": "application/json",
    })
    with urlopen(req, timeout=100) as response:
        return response.read()


def search(payload):
    # A failed or ambiguous POST must be reconciled in Apify Console before retrying.
    raw = request(f"acts/{ACTOR}/runs?waitForFinish=60&timeout=90&maxTotalChargeUsd=0.05",
                  body=payload)
    run = json.loads(raw)["data"]
    if run["status"] != "SUCCEEDED":
        raise SystemExit(f"Run {run['id']} is {run['status']}. Inspect it in Apify Console.")
    return run
