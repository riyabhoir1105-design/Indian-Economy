import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Indian Economy ML Dashboard",
    page_icon="🇮🇳",
    layout="wide"
)

model = joblib.load("economy.pkl")
economy = pd.read_excel("Indian_Economy.xlsx")

st.markdown("""
<style>

.stApp {
    background-color: #f5f7f4;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.main-title {
    font-size: 36px;
    font-weight: 700;
    color: #30343f;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 16px;
    color: #7b827f;
    margin-bottom: 35px;
}

.section-title {
    font-size: 13px;
    font-weight: 700;
    color: #638071;
    letter-spacing: 1.5px;
    margin-bottom: 10px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 10px;
    border: 1px solid #e2e7e3;
    min-height: 150px;
}

.card-title {
    color: #59635e;
    font-size: 15px;
}

.card-value {
    color: #35423c;
    font-size: 30px;
    font-weight: 600;
    margin-top: 10px;
}

.card-text {
    color: #8a918d;
    font-size: 13px;
    margin-top: 5px;
}

.result {
    background-color: #e0f3e7;
    border-radius: 10px;
    padding: 25px;
    border: 1px solid #cfe7d7;
}

.result-title {
    color: #16833d;
    font-size: 16px;
}

.result-value {
    color: #35423c;
    font-size: 35px;
    font-weight: 600;
    margin-top: 10px;
}

.stButton > button {
    background-color: #1d5948;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 10px 25px;
    font-size: 16px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #26725d;
    color: white;
}

div[data-testid="stNumberInput"] input {
    background-color: #eef1f5;
}

</style>
""", unsafe_allow_html=True)


# Header

st.markdown(
    '<div class="main-title">Indian Economy ML Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Economic data and machine-learning imports predictions.</div>',
    unsafe_allow_html=True
)


# Economic indicators

st.markdown(
    '<div class="section-title">ECONOMIC INDICATORS</div>',
    unsafe_allow_html=True
)

gdp_total = economy["GDP_Lakh_Crore"].sum()
imports_total = economy["Imports_Crore"].sum()
exports_total = economy["Exports_Crore"].sum()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">GDP</div>
        <div class="card-value">{gdp_total:,.2f}</div>
        <div class="card-text">Total in dataset, Lakh Crore</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">Imports</div>
        <div class="card-value">{imports_total:,.2f}</div>
        <div class="card-text">Total in dataset, Crore</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">Exports</div>
        <div class="card-value">{exports_total:,.2f}</div>
        <div class="card-text">Total in dataset, Crore</div>
    </div>
    """, unsafe_allow_html=True)


st.write("")


# Charts

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        '<div class="section-title">TREND</div>',
        unsafe_allow_html=True
    )

    st.subheader("GDP by Year")

    gdp_data = economy.groupby("Year")["GDP_Lakh_Crore"].sum()

    st.bar_chart(gdp_data)


with col2:

    st.markdown(
        '<div class="section-title">TRADE</div>',
        unsafe_allow_html=True
    )

    st.subheader("Imports by Year")

    imports_data = economy.groupby("Year")["Imports_Crore"].sum()

    st.bar_chart(imports_data)


st.write("")


# Prediction

col1, col2 = st.columns([1, 1])

with col1:

    st.markdown(
        '<div class="section-title">MACHINE LEARNING</div>',
        unsafe_allow_html=True
    )

    st.header("Predict Imports")

    st.write(
        "Enter a year to get an estimate from the trained model."
    )

    year = st.number_input(
        "Enter Year",
        min_value=1000,
        max_value=9999,
        value=2039,
        step=1
    )

    predict = st.button("Predict Imports →")


with col2:

    st.markdown(
        '<div class="section-title">PREDICTION RESULT</div>',
        unsafe_allow_html=True
    )

    if predict:

        input_data = pd.DataFrame({
            "Year": [year]
        })

        prediction = model.predict(input_data)

        result = float(prediction[0])

        st.markdown(f"""
        <div class="result">
            <div class="result-title">
                Prediction for {int(year)}
            </div>
            <div class="result-value">
                {result:,.2f} Crore
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.caption(
            "Predicted Imports_Crore using the trained Linear Regression model."
        )

    else:

        st.info("Enter a year and click Predict Imports.")


st.write("")

st.caption("Indian Economy ML | Dashboard")