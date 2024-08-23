import cv2
import numpy as np
import os
import mediapipe as mp
import time


# Load the face detection model
mp_face_detection = mp.solutions.face_detection
detector = mp_face_detection.FaceDetection(min_detection_confidence=0.7)


screenshot_dir = 'screenshots'
os.makedirs(screenshot_dir, exist_ok=True)
last_screenshot_time = time.time()
screenshot_interval = 5  # seconds

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = detector.process(frame_rgb)

    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(frame, bbox, (255, 0, 255), 2)
            cv2.putText(frame, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

    # Save a screenshot every 5 seconds
    current_time = time.time()
    if current_time - last_screenshot_time > screenshot_interval:
        screenshot_path = os.path.join(screenshot_dir, f'screenshot_{int(current_time)}.png')
        cv2.imwrite(screenshot_path, frame)
        last_screenshot_time = current_time

    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


