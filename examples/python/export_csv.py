"""Export an existing Dataset without starting an Actor."""
import argparse
from pathlib import Path
import re

from common import request

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset_id")
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9]+", args.dataset_id):
        parser.error("Enter the Dataset ID from your Actor run.")
    args.destination.write_bytes(request(f"datasets/{args.dataset_id}/items?format=csv"))
