import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Indian Economy ML Dashboard",
    page_icon="🇮🇳",
    layout="wide"
)

# Load files
model = joblib.load("economy.pkl")
economy = pd.read_excel("Indian_Economy.xlsx")


# CSS only
st.markdown("""
<style>

.stApp {
    background-color: #f5f7f4;
}

.block-container {
    max-width: 1080px;
    padding-top: 0;
}

header[data-testid="stHeader"] {
    background-color: #173f35;
}

.title {
    color: #202a27;
    font-size: 30px;
    font-weight: 650;
}

.subtitle {
    color: #707b76;
    font-size: 14px;
}

.section {
    color: #638071;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 1px;
}

div[data-testid="stMetric"] {
    background-color: white;
    border: 1px solid #e3e8e4;
    border-radius: 7px;
    padding: 20px;
}

div[data-testid="stMetricValue"] {
    color: #35423c;
}

div[data-testid="stMetricLabel"] {
    color: #53615a;
}

.stButton > button {
    background-color: #173f35;
    color: white;
    border: none;
    border-radius: 5px;
    width: 100%;
}

.stButton > button:hover {
    background-color: #235546;
    color: white;
}

.result-box {
    background-color: white;
    border: 1px solid #e3e8e4;
    border-radius: 7px;
    padding: 25px;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)


# Top heading
st.markdown("### 🇮🇳 Indian Economy ML")
st.caption("Python Model • Economy data loaded")

st.markdown(
    '<p class="section">ECONOMIC INDICATORS</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">Indian Economy ML Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Economic data and machine-learning imports predictions.</div>',
    unsafe_allow_html=True
)

st.write("")


# Calculate totals
gdp_total = economy["GDP_Lakh_Crore"].sum()
imports_total = economy["Imports_Crore"].sum()
exports_total = economy["Exports_Crore"].sum()


# Metric cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="GDP",
        value=f"{gdp_total:,.2f}",
        help="Total GDP in the dataset"
    )
    st.caption("Total in dataset, Lakh Crore")

with col2:
    st.metric(
        label="Imports",
        value=f"{imports_total:,.2f}",
        help="Total Imports in the dataset"
    )
    st.caption("Total in dataset, Crore")

with col3:
    st.metric(
        label="Exports",
        value=f"{exports_total:,.2f}",
        help="Total Exports in the dataset"
    )
    st.caption("Total in dataset, Crore")


st.write("")


# Charts
col1, col2 = st.columns(2)

with col1:

    st.markdown(
        '<p class="section">TREND</p>',
        unsafe_allow_html=True
    )

    st.subheader("GDP by year")

    st.caption("Lakh Crore")

    gdp_data = economy.groupby("Year")["GDP_Lakh_Crore"].sum()

    st.bar_chart(gdp_data)


with col2:

    st.markdown(
        '<p class="section">TRADE</p>',
        unsafe_allow_html=True
    )

    st.subheader("Imports by year")

    st.caption("Crore")

    imports_data = economy.groupby("Year")["Imports_Crore"].sum()

    st.bar_chart(imports_data)


st.write("")


# Prediction section
col1, col2 = st.columns([1.1, 0.9])

with col1:

    st.markdown(
        '<p class="section">MACHINE LEARNING</p>',
        unsafe_allow_html=True
    )

    st.subheader("Predict imports")

    st.caption(
        "Enter a year to get an estimate from the trained model."
    )

    year = st.number_input(
        "Year",
        min_value=1000,
        max_value=9999,
        value=2025,
        step=1
    )

    predict_button = st.button("Predict Imports →")


with col2:

    st.markdown(
        '<p class="section">PREDICTION RESULT</p>',
        unsafe_allow_html=True
    )

    if predict_button:

        input_data = pd.DataFrame({
            "Year": [year]
        })

        prediction = model.predict(input_data)

        result = float(prediction[0])

        st.success(
            f"Prediction for {int(year)}"
        )

        st.metric(
            "Predicted Imports",
            f"{result:,.2f} Crore"
        )

        st.caption(
            "Predicted Imports_Crore using the trained "
            "Linear Regression model."
        )

    else:

        st.info(
            "Enter a year and click Predict Imports."
        )


# Footer
st.write("")

st.caption("Indian Economy ML | Dashboard")