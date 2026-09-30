import streamlit as st
import pandas as pd
import joblib

st.title("Indian Economy ML Dashboard")

data = pd.read_excel("Indian_Economy.xlsx")

model = joblib.load("economy.pkl")

st.write("### Economy Data")
st.dataframe(data)

st.write("### Predict Imports")

year = st.number_input("Enter Year", 2020, 2100, 2039)

if st.button("Predict Imports"):

    x = pd.DataFrame({"Year": [year]})

    prediction = model.predict(x)

    st.success(f"Predicted Imports: {prediction[0]:,.2f} Crore")

st.write("### GDP by Year")

gdp = data.groupby("Year")["GDP_Lakh_Crore"].sum()

st.line_chart(gdp)

st.write("### Imports by Year")

imports = data.groupby("Year")["Imports_Crore"].sum()

st.line_chart(imports)