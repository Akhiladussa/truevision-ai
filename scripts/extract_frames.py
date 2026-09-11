import cv2
import json
import os

METADATA_PATH = "data/raw/metadata.json"
VIDEO_DIR = "data/raw"
OUTPUT_DIR = "data/processed/frames"
FRAMES_PER_VIDEO = 10

with open(METADATA_PATH, "r") as f:
    metadata = json.load(f)

for filename, info in metadata.items():
    video_path = os.path.join(VIDEO_DIR, filename)
    if not os.path.exists(video_path):
        continue

    label = "real" if info["label"] == "REAL" else "fake"
    video_name = os.path.splitext(filename)[0]
    out_folder = os.path.join(OUTPUT_DIR, label, video_name)
    os.makedirs(out_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    step = max(total_frames // FRAMES_PER_VIDEO, 1)

    count, saved = 0, 0
    while cap.isOpened() and saved < FRAMES_PER_VIDEO:
        ret, frame = cap.read()
        if not ret:
            break
        if count % step == 0:
            frame_path = os.path.join(out_folder, f"frame_{saved:03d}.jpg")
            cv2.imwrite(frame_path, frame)
            saved += 1
        count += 1
    cap.release()
    print(f"{filename}: extracted {saved} frames -> {label}")

print("Frame extraction complete.")