import json
import os
import subprocess

METADATA_PATH = "data/raw/metadata.json"
VIDEO_DIR = "data/raw"
OUTPUT_DIR = "data/processed/audio"
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"

with open(METADATA_PATH, "r") as f:
    metadata = json.load(f)

for filename, info in metadata.items():
    video_path = os.path.join(VIDEO_DIR, filename)
    if not os.path.exists(video_path):
        continue

    label = "real" if info["label"] == "REAL" else "fake"
    audio_name = os.path.splitext(filename)[0] + ".wav"
    out_path = os.path.join(OUTPUT_DIR, label, audio_name)

    command = [FFMPEG_PATH, "-y", "-i", video_path, "-q:a", "0", "-map", "a", out_path]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"{filename}: audio extracted -> {label}")
    else:
        print(f"{filename}: FAILED (may have no audio track)")

print("Audio extraction complete.")