import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv("datasets/gestures.csv", header=None)

# Split features and labels
X = data.iloc[:, :-1]   # all columns except last
y = data.iloc[:, -1]    # last column (gesture label)

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Check accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Save model
with open("models/gesture_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")