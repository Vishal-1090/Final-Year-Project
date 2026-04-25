from fastapi import FastAPI, Body
import pickle
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load trained model
with open("models/gesture_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.get("/")
def home():
    return {"message": "Gesture API running"}


@app.post("/predict")
def predict_gesture(data: list = Body(...)):
    try:
        # Debug (you can remove later)
        print("Received length:", len(data))

        # Validate input
        if len(data) != 42:
            return {"gesture": "invalid"}

        # Convert to numpy array
        arr = np.array(data).reshape(1, -1)

        # Predict
        prediction = model.predict(arr)[0]

        return {"gesture": prediction}

    except Exception as e:
        print("Error:", e)
        return {"gesture": "error"}
    
latest_gesture = "none"

@app.post("/update")
def update_gesture(data: dict):
    global latest_gesture
    latest_gesture = data["gesture"]
    return {"status": "updated"}

@app.get("/gesture")
def get_gesture():
    return {"gesture": latest_gesture}