# 📊 Investment Portfolio Analytics & Recommendation System

An interactive **Streamlit web application** that analyzes investment portfolios from uploaded CSV files and generates insights on **risk segmentation, diversification, and portfolio performance**.

This project automates data cleaning, calculates investment ratios, segments clients based on their risk profile, and provides actionable recommendations to improve portfolio balance and risk-adjusted returns.

---

## 🚀 Features

- 📂 **CSV Upload Support** – Upload your own portfolio dataset directly in the app  
- 🧮 **Automated Data Cleaning** – Handles missing values and computes total investment & ratios  
- 🧠 **Client Risk Segmentation** – Classifies investors as Low, Moderate, or High Risk based on equity exposure and volatility  
- 📈 **Dynamic Visualizations** – Interactive charts showing portfolio distribution and returns  
- 💡 **Investment Recommendations** – Suggests diversification strategies to balance risk vs. return  
- 🌐 **Streamlit Interface** – Lightweight, clean UI for instant insights without any backend setup  

---

## 🧰 Tech Stack

- **Frontend / Dashboard:** Streamlit  
- **Data Handling:** Pandas, NumPy  
- **Visualization:** Matplotlib  
- **Language:** Python 3.9+

---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/investment-portfolio-analytics.git
cd investment-portfolio-analytics
pip install -r requirements.txt
```

---

## ▶️ Run the App

Run the Streamlit web app locally:

```bash
streamlit run app.py
```

Then open your browser at [http://localhost:8501](http://localhost:8501)

---

## 🧾 Input Data Format

Upload a `.csv` file with the following columns:

| Column | Description |
|--------|--------------|
| `Client_ID` | Unique identifier for each client |
| `Age` | Age of the investor |
| `Annual_Income` | Annual income of the investor |
| `Equity_Investment` | Amount invested in equities |
| `Bond_Investment` | Amount invested in bonds |
| `MutualFunds` | Amount invested in mutual funds |
| `Avg_Return_Percent` | Average annual portfolio return (%) |
| `Volatility_Percent` | Risk or fluctuation measure (%) |

Example (first few rows):

| Client_ID | Age | Annual_Income | Equity_Investment | Bond_Investment | MutualFunds | Avg_Return_Percent | Volatility_Percent |
|------------|-----|---------------|------------------|----------------|--------------|--------------------|--------------------|
| 101 | 45 | 900000 | 450000 | 250000 | 200000 | 8.5 | 6.2 |
| 102 | 32 | 650000 | 300000 | 150000 | 200000 | 10.1 | 7.8 |

---

## 📊 App Overview

Once you upload your dataset:
1. The app computes **Equity, Bond, and Mutual Fund ratios**
2. Segments clients into **Low / Moderate / High risk profiles**
3. Displays charts for:
   - Portfolio composition by risk
   - Average returns per profile
   - Asset allocation pie chart
4. Generates diversification suggestions:
   - ⚠️ Too equity-heavy → add bonds/funds  
   - 💰 Too conservative → explore equities  
   - ✅ Balanced → well-diversified

---

## 🧠 Future Enhancements

- Add **Sharpe Ratio & Beta** metrics for deeper financial insights  
- Integrate **live market data APIs** for portfolio updates  
- Export **PDF reports** summarizing key analytics  

---

## 👨‍💻 Author

**Gyan Vardhan**  
📧 gyanv.official@gmail.com  

---

## 📝 License

This project is licensed under the MIT License — feel free to use and modify for learning purposes.
