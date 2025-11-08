# data_utils.py
import pandas as pd
import numpy as np

def load_and_prepare(csv_file):
    df = pd.read_csv(csv_file)
    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)
    
    df['Total_Investment'] = df[['Equity_Investment','Bond_Investment','MutualFunds']].sum(axis=1)
    df['Equity_Ratio'] = df['Equity_Investment'] / df['Total_Investment']
    df['Bond_Ratio'] = df['Bond_Investment'] / df['Total_Investment']
    df['MF_Ratio'] = df['MutualFunds'] / df['Total_Investment']
    
    # Risk segmentation
    def risk(row):
        if row['Equity_Ratio'] > 0.6: return "High Risk"
        elif row['Equity_Ratio'] > 0.3: return "Moderate Risk"
        else: return "Low Risk"
    df['Risk_Profile'] = df.apply(risk, axis=1)
    
    return df
