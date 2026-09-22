import cv2
import mediapipe as mp
import os

INPUT_DIR = "data/processed/frames"
OUTPUT_DIR = "data/processed/faces"

mp_face_detection = mp.solutions.face_detection
face_detector = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)

def process_folder(label):
    input_label_dir = os.path.join(INPUT_DIR, label)
    output_label_dir = os.path.join(OUTPUT_DIR, label)
    os.makedirs(output_label_dir, exist_ok=True)

    for video_folder in os.listdir(input_label_dir):
        video_path = os.path.join(input_label_dir, video_folder)
        out_video_path = os.path.join(output_label_dir, video_folder)
        os.makedirs(out_video_path, exist_ok=True)

        for frame_file in os.listdir(video_path):
            frame_path = os.path.join(video_path, frame_file)
            image = cv2.imread(frame_path)
            if image is None:
                continue
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_detector.process(rgb_image)

            if results.detections:
                h, w, _ = image.shape
                box = results.detections[0].location_data.relative_bounding_box
                x1 = max(int(box.xmin * w), 0)
                y1 = max(int(box.ymin * h), 0)
                x2 = min(int((box.xmin + box.width) * w), w)
                y2 = min(int((box.ymin + box.height) * h), h)
                face_crop = image[y1:y2, x1:x2]
                if face_crop.size > 0:
                    out_path = os.path.join(out_video_path, frame_file)
                    cv2.imwrite(out_path, face_crop)

        print(f"Processed faces for: {video_folder} ({label})")

process_folder("real")
process_folder("fake")
print("Face detection complete.")