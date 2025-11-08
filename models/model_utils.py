# model_utils.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

def train_model(df):
    features = ['Age','Annual_Income','Equity_Ratio','Bond_Ratio','MF_Ratio','Volatility_Percent']
    target = 'Avg_Return_Percent'
    
    X = df[features]
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=150, random_state=42)
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    print("R² Score:", round(r2_score(y_test, preds), 3))
    print("MAE:", round(mean_absolute_error(y_test, preds), 3))
    
    joblib.dump(model, "portfolio_model.pkl")
    print("✅ Model saved as portfolio_model.pkl")
    return model

def predict_returns(model, df):
    features = ['Age','Annual_Income','Equity_Ratio','Bond_Ratio','MF_Ratio','Volatility_Percent']
    df['Predicted_Return'] = model.predict(df[features])
    return df
