import os
import json

FILE = "memory.json"

def load_last_ts():
    if not os.path.exists(FILE):
        return 0

    with open(FILE, "r") as f:
        data = json.load(f)
        return data.get("last_ts", 0)

def save_last_ts(ts):
    with open(FILE, "w") as f:
        json.dump({"last_ts": ts}, f)
