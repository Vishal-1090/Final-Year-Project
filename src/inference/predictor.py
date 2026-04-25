import pickle
import numpy as np

with open("models/gesture_model.pkl", "rb") as f:
    model = pickle.load(f)

def detect_gesture_from_landmarks(landmarks):
    try:
        print("Landmarks length:", len(landmarks))  # 👈 debug

        if len(landmarks) != 42:
            return "unknown"

        arr = np.array(landmarks).reshape(1, -1)
        prediction = model.predict(arr)[0]
        return prediction

    except Exception as e:
        print("Error:", e)
        return "error"