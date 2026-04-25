import cv2
import csv
import mediapipe as mp

# Setup MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# 👇 Change this label for each gesture
GESTURE_LABEL = "point_right"

# Open CSV file
file = open("datasets/gestures.csv", "a", newline="")
writer = csv.writer(file)

# Start camera
cap = cv2.VideoCapture(0)

print("Press 's' to save data, 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            landmarks = []
            for lm in handLms.landmark:
                landmarks.extend([lm.x, lm.y])

            key = cv2.waitKey(1)

            if key == ord('s'):
                writer.writerow(landmarks + [GESTURE_LABEL])
                print(f"Saved: {GESTURE_LABEL}")

    cv2.imshow("Recorder", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
file.close()
cv2.destroyAllWindows()