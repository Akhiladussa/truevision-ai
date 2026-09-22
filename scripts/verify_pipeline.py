import os

paths_to_check = [
    "data/processed/frames/real",
    "data/processed/frames/fake",
    "data/processed/faces/real",
    "data/processed/faces/fake",
    "data/processed/audio/real",
    "data/processed/audio/fake",
]

for path in paths_to_check:
    if os.path.exists(path):
        count = sum(len(files) for _, _, files in os.walk(path))
        print(f"{path}: {count} files")
    else:
        print(f"{path}: MISSING")