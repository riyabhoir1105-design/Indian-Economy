import joblib
import pandas as pd

model = joblib.load("economy.pkl")

print("Model loaded successfully")

year = int(input("Enter Year: "))

data = pd.DataFrame({
    "Year": [year]
})

prediction = model.predict(data)

print("Predicted Imports:", prediction[0])