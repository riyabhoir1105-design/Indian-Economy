from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("economy.pkl")

data = pd.read_excel("Indian_Economy.xlsx")
yearly_data = data.groupby("Year")[["GDP_Lakh_Crore", "Imports_Crore"]].sum().sort_index()


@app.route("/predict", methods=["POST"])
def predict():

    value = request.json["year"]

    x = pd.DataFrame({
        "Year": [value]
    })

    prediction = model.predict(x)

    return jsonify({
        "prediction": float(prediction[0])
    })


@app.route("/data")
def get_data():

    return jsonify({
        "gdp": float(data["GDP_Lakh_Crore"].sum()),
        "imports": float(data["Imports_Crore"].sum()),
        "exports": float(data["Exports_Crore"].sum()),
        "years": [
            {
                "year": int(year),
                "gdp": float(values["GDP_Lakh_Crore"]),
                "imports": float(values["Imports_Crore"]),
            }
            for year, values in yearly_data.iterrows()
        ],
    })


if __name__ == "__main__":
    app.run(debug=True)