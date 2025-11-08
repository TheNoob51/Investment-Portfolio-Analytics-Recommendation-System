import pandas as pd
import random

rows = []
for i in range(1, 1001):
    age = random.randint(25, 65)
    income = random.randint(400000, 2000000)
    equity = random.randint(100000, 800000)
    bonds = random.randint(100000, 800000)
    mf = random.randint(100000, 800000)
    total = equity + bonds + mf
    volatility = round(random.uniform(2, 12), 2)
    avg_return = round((equity/total)*10 + (mf/total)*7 + (bonds/total)*5 - volatility*0.1, 2)
    rows.append([i, age, income, equity, bonds, mf, avg_return, volatility])

df = pd.DataFrame(rows, columns=[
    'Client_ID', 'Age', 'Annual_Income', 'Equity_Investment',
    'Bond_Investment', 'MutualFunds', 'Avg_Return_Percent', 'Volatility_Percent'
])
df.to_csv('portfolio_sample.csv', index=False)
print("✅ portfolio_sample.csv generated.")
