import pandas as pd

def analyze_financials(df: pd.DataFrame):
    revenue = df[df['type'] == 'revenue']['amount'].sum()
    expenses = df[df['type'] == 'expense']['amount'].sum()
    profit = revenue - expenses

    monthly = df.groupby('month')['amount'].sum()

    return {
        "revenue": float(revenue),
        "expenses": float(expenses),
        "profit": float(profit),
        "monthly_trend": monthly.to_dict()
    }
