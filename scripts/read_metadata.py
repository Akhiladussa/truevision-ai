
import json

with open("data/raw/metadata.json", "r") as f:
    metadata = json.load(f)

real_count = 0
fake_count = 0

for filename, info in metadata.items():
    if info["label"] == "REAL":
        real_count += 1
    else:
        fake_count += 1

print(f"Total videos: {len(metadata)}")
print(f"REAL videos: {real_count}")
print(f"FAKE videos: {fake_count}")