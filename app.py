import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from models.data_utils import load_and_prepare
from models.model_utils import predict_returns

st.set_page_config(page_title="Investment Portfolio AI", layout="wide")
st.title("💹 Investment Portfolio Analytics & Recommendation System")
st.markdown("Upload a portfolio CSV to analyze, predict returns, and get investment recommendations.")

uploaded_file = st.file_uploader("Upload Portfolio CSV", type=["csv"])

if uploaded_file:
    df = load_and_prepare(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Load model
    model = joblib.load("models/portfolio_model.pkl")
    df = predict_returns(model, df)
    
    st.subheader("Predicted Returns by Risk Profile")
    avg_pred = df.groupby('Risk_Profile')['Predicted_Return'].mean().reset_index()
    st.bar_chart(avg_pred.set_index('Risk_Profile'))
    
    st.subheader("Client Recommendations")
    def advice(row):
        if row['Equity_Ratio'] > 0.6:
            return "Reduce equity exposure; consider bonds or mutual funds."
        elif row['Equity_Ratio'] < 0.3:
            return "Increase equity exposure for higher growth potential."
        else:
            return "Portfolio appears balanced."
    df['Advice'] = df.apply(advice, axis=1)
    st.dataframe(df[['Client_ID','Risk_Profile','Predicted_Return','Advice']].head(10))
    
    st.download_button("Download Analyzed Data", df.to_csv(index=False), "portfolio_analysis.csv")
else:
    st.info("Please upload a CSV file to start the analysis.")
